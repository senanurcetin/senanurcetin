#!/usr/bin/env python3
"""Review and optionally synchronize GitHub repository metadata using gh CLI.

Dry-run by default. Requires an authenticated gh installation for GitHub writes.
Does not touch code, branches, workflows, releases or repository visibility.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CONFIG = Path(__file__).resolve().parents[1] / "config" / "repository-metadata.json"
TOPIC = re.compile(r"^[a-z0-9][a-z0-9-]{0,49}$")


def api(method: str, path: str, payload: dict | None = None):
    cmd = [
        "gh", "api", "--method", method,
        "--header", "Accept: application/vnd.github+json", path,
    ]
    if payload is not None:
        cmd.extend(["--input", "-"])
    try:
        proc = subprocess.run(
            cmd, input=json.dumps(payload) if payload is not None else None,
            capture_output=True, text=True, check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError("GitHub CLI is unavailable; install gh and run gh auth login") from exc
    if proc.returncode:
        raise RuntimeError(f"{path}: {proc.stderr.strip() or 'GitHub API request failed'}")
    return json.loads(proc.stdout) if proc.stdout.strip() else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write proposed changes to GitHub")
    parser.add_argument("--overwrite", action="store_true",
                        help="Replace existing nonempty descriptions/topics, not just fill gaps")
    parser.add_argument("--repo", action="append", default=[], help="Select repo name; repeatable")
    parser.add_argument("--previews", action="store_true",
                        help="Print authentic screenshot URLs and manual Social Preview settings links")
    args = parser.parse_args()
    config = json.loads(CONFIG.read_text(encoding="utf-8"))
    owner = config["owner"]
    records = config["repositories"]
    names = {item["name"] for item in records}
    unknown = set(args.repo) - names
    if unknown:
        parser.error(f"Unknown repository names: {', '.join(sorted(unknown))}")
    selected = [x for x in records if not args.repo or x["name"] in args.repo]
    changes = 0
    failures = 0

    for spec in selected:
        name = spec["name"]
        full = f"{owner}/{name}"
        settings = f"https://github.com/{full}/settings"
        if args.previews and spec.get("social_preview"):
            path = spec["social_preview"]
            print(f"PREVIEW {full}: https://raw.githubusercontent.com/{full}/{spec.get('default_branch', 'main')}/{path}")
            print(f"  Upload via {settings} (Social Preview); this tool does not upload media.")
        elif args.previews:
            print(f"PREVIEW {full}: no verified authentic PNG/JPG candidate")
        if args.previews and not args.apply:
            continue
        try:
            existing = api("GET", f"repos/{full}")
            proposed: dict[str, str] = {}
            description = spec.get("description")
            if description and (args.overwrite or not existing.get("description")):
                if existing.get("description") != description:
                    proposed["description"] = description
            homepage = spec.get("homepage")
            if homepage and (args.overwrite or not existing.get("homepage")):
                if existing.get("homepage") != homepage:
                    proposed["homepage"] = homepage
            topics = spec.get("topics")
            topics_write = False
            if topics is not None:
                if len(topics) > 20 or len(set(topics)) != len(topics) or any(
                    not TOPIC.fullmatch(t) for t in topics
                ):
                    raise ValueError(f"Invalid topics in manifest for {full}")
                old_topics = existing.get("topics") or []
                topics_write = (args.overwrite or not old_topics) and old_topics != topics
            if not proposed and not topics_write:
                print(f"OK      {full}: no eligible metadata changes")
                continue
            print(f"{'APPLY' if args.apply else 'PLAN '}    {full}: "
                  f"{list(proposed)}{' + topics' if topics_write else ''}")
            if args.apply:
                if proposed:
                    api("PATCH", f"repos/{full}", proposed)
                if topics_write:
                    api("PUT", f"repos/{full}/topics", {"names": topics})
            changes += 1
        except (RuntimeError, ValueError, json.JSONDecodeError) as exc:
            failures += 1
            print(f"ERROR   {full}: {exc}", file=sys.stderr)

    print(f"\n{'Applied' if args.apply else 'Planned'}: {changes} repositories; errors: {failures}.")
    if not args.apply:
        print("No remote metadata was changed. Run with --apply when ready.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
