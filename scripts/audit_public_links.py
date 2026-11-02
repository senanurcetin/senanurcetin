#!/usr/bin/env python3
"""Opt-in, read-only HTTP link audit for public portfolio documentation.

This script does NOT run in CI, modify repositories, deploy apps, or authenticate to
third-party services. HTTP status is a reachability observation, not a reliability
or production-readiness guarantee.
"""
from __future__ import annotations

import argparse
import collections
import concurrent.futures
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_PATHS = (
    "README.md",
    "docs/REVIEWER_GUIDE.md",
    "docs/PROJECT_REVIEW_INDEX.md",
    "docs/PROJECT_CATALOG.md",
    "docs/REPOSITORY_FINISHING_GUIDE.md",
    "docs/site-sync-brief.md",
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\((https?://[^)\s]+)\)")
USER_AGENT = "Mozilla/5.0 (compatible; PortfolioLinkAudit/1.0)"
RETRY_GET = frozenset((403, 404, 405, 429, 501))


def public_links() -> dict[str, list[str]]:
    sources: dict[str, set[str]] = collections.defaultdict(set)

    def add(url: object, source: str) -> None:
        if not isinstance(url, str):
            return
        candidate = url.strip().rstrip(".,")
        parsed = urllib.parse.urlsplit(candidate)
        if parsed.scheme == "https" and parsed.hostname:
            sources[candidate].add(source)

    for filename in MARKDOWN_PATHS:
        path = ROOT / filename
        if not path.is_file():
            raise FileNotFoundError(f"Missing public documentation: {filename}")
        for link in MARKDOWN_LINK.findall(path.read_text(encoding="utf-8")):
            add(link, filename)

    portfolio = json.loads((ROOT / "docs/portfolio-manifest.json").read_text(encoding="utf-8"))
    for item in (*portfolio.get("lead_projects", ()), *portfolio.get("supporting_evidence", ())):
        for key in ("repo_url", "demo_url", "release_url"):
            add(item.get(key), f"docs/portfolio-manifest.json:{item.get('repo')}:{key}")

    metadata = json.loads((ROOT / "config/repository-metadata.json").read_text(encoding="utf-8"))
    for item in metadata.get("repositories", ()):
        add(item.get("homepage"), f"config/repository-metadata.json:{item.get('name')}:homepage")

    return {url: sorted(locations) for url, locations in sorted(sources.items())}


def request_status(url: str, method: str, timeout: float) -> tuple[int | None, str]:
    request = urllib.request.Request(
        url, method=method, headers={"User-Agent": USER_AGENT, "Accept": "text/html,*/*"}
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if method == "GET":
                response.read(1024)
            return response.status, response.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.geturl()
    except (TimeoutError, OSError, ValueError) as exc:
        return None, type(exc).__name__


def is_authenticated_github_control(url: str) -> bool:
    """Repository Settings are owner-only and intentionally 404 when signed out."""
    parsed = urllib.parse.urlsplit(url)
    segments = parsed.path.strip("/").split("/")
    return (
        parsed.scheme == "https"
        and parsed.hostname == "github.com"
        and len(segments) >= 3
        and segments[2] == "settings"
    )


def audit(item: tuple[str, list[str]], timeout: float) -> dict[str, object]:
    url, locations = item
    if is_authenticated_github_control(url):
        return {
            "url": url,
            "status": None,
            "verdict": "auth-required",
            "destination": url,
            "sources": locations,
        }
    status, destination = request_status(url, "HEAD", timeout)
    if status in RETRY_GET or status is None:
        status, destination = request_status(url, "GET", timeout)

    if status is None:
        verdict = "inconclusive"
    elif 200 <= status < 300:
        verdict = "reachable"
    elif status in (401, 403, 429, 999):
        verdict = "access-restricted"
    elif status in (404, 410):
        verdict = "candidate-broken"
    else:
        verdict = "review"
    return {
        "url": url,
        "status": status,
        "verdict": verdict,
        "destination": destination,
        "sources": locations,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--timeout", type=float, default=6.0, help="Timeout per HTTP request")
    parser.add_argument("--workers", type=int, default=6, help="Maximum parallel link probes")
    parser.add_argument("--limit", type=int, default=120, help="Hard cap to avoid runaway web requests")
    parser.add_argument("--json", action="store_true", help="Print full JSON report")
    args = parser.parse_args()
    if not 1 <= args.workers <= 12 or not 0 < args.timeout <= 30 or not 1 <= args.limit <= 500:
        parser.error("Require workers 1..12, timeout 0..30 and limit 1..500")

    links = public_links()
    if len(links) > args.limit:
        parser.error(f"Found {len(links)} URLs; increase --limit intentionally")
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda item: audit(item, args.timeout), links.items()))
    counts = dict(collections.Counter(row["verdict"] for row in results))

    if args.json:
        print(json.dumps({"count": len(results), "verdicts": counts, "results": results}, indent=2))
    else:
        print(f"Audited {len(results)} public URLs; verdicts: {counts}")
        for row in results:
            if row["verdict"] != "reachable":
                print(f"{row['verdict']} | HTTP {row['status']} | {row['url']}")
                print(f"  References: {', '.join(row['sources'])}")
        print("A bot-blocked URL or sleeping deployment needs manual browser review.")
    # Network failures are observations, not blocking documentation-CI failures.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
