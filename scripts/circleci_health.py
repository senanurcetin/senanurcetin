#!/usr/bin/env python3
"""Read-only CircleCI status inventory via authenticated GitHub commit statuses.

No CircleCI token or GitHub Actions runner is required. A GitHub token is needed
for private repositories. This reports status notifications, not job-log coverage.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "circleci-projects.json"
API = "https://api.github.com"
SKIP = re.compile(r"\[(?:skip ci|ci skip)\]", re.I)


def classify(message: str, statuses: list[dict], required: list[str]) -> tuple[str, list[str]]:
    """Choose a defensible state for all expected CircleCI status contexts."""
    latest = {}
    for status in statuses:
        context = status.get("context", "")
        if context.startswith("ci/circleci:") and context not in latest:
            latest[context] = status.get("state", "unknown")
    if not latest and SKIP.search(message):
        return "SKIPPED", list(required)
    missing = [name for name in required if name not in latest]
    if any(latest.get(name) in ("failure", "error") for name in required):
        return "FAILED", missing
    if any(latest.get(name) == "pending" for name in required):
        return "PENDING", missing
    if missing:
        return "MISSING", missing
    if all(latest.get(name) == "success" for name in required):
        return "PASSED", []
    return "UNKNOWN", missing


def get_json(path: str, token: str | None) -> dict:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "portfolio-circleci-health/1.0",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urlopen(Request(API + path, headers=headers), timeout=20) as response:
        return json.load(response)


def inspect(repo: str, expected: list[str], token: str | None) -> dict:
    try:
        commit = get_json(f"/repos/{repo}/commits/main", token)
        sha = commit["sha"]
        statuses = get_json(f"/repos/{repo}/commits/{sha}/status", token)["statuses"]
        message = commit["commit"]["message"]
        state, missing = classify(message, statuses, expected)
        return {
            "repo": repo, "sha": sha, "state": state, "missing_contexts": missing,
            "ci_links": [
                s.get("target_url") for s in statuses
                if s.get("context") in expected and s.get("target_url")
            ],
            "other_failures": sorted(set(
                s.get("context", "") for s in statuses
                if s.get("state") in ("failure", "error")
                and not s.get("context", "").startswith("ci/circleci:")
            )),
        }
    except (HTTPError, URLError, TimeoutError, ValueError, KeyError) as exc:
        # Never include secrets or the raw API error body in a status report.
        code = getattr(exc, "code", None)
        reason = f"HTTP {code}" if code else type(exc).__name__
        return {
            "repo": repo, "sha": None, "state": "UNAVAILABLE", "reason": reason,
            "missing_contexts": expected, "ci_links": [], "other_failures": [],
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only CircleCI inventory")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--strict", action="store_true", help="Fail unless every status is PASSED")
    args = parser.parse_args()
    projects = json.loads(MANIFEST.read_text(encoding="utf-8"))["projects"]
    rows = [
        inspect(project["repo"], project["contexts"], os.getenv("GITHUB_TOKEN"))
        for project in projects
    ]
    if args.format == "json":
        print(json.dumps({"projects": rows}, indent=2, ensure_ascii=False))
    else:
        print("| Repository | Last main SHA | CircleCI | Missing contexts | Other failures |")
        print("|---|---|---|---|---|")
        for row in rows:
            sha = row["sha"][:10] if row["sha"] else "—"
            missing = ", ".join(row["missing_contexts"]) or "—"
            others = ", ".join(row["other_failures"]) or "—"
            print(f'| {row["repo"]} | {sha} | {row["state"]} | {missing} | {others} |')
        print("\nPASSED = all expected CircleCI contexts succeeded on this SHA, not production health.")
        print("SKIPPED = explicit [skip ci] commit; inspect preceding tested code separately.")
    return int(args.strict and any(row["state"] != "PASSED" for row in rows))


if __name__ == "__main__":
    sys.exit(main())
