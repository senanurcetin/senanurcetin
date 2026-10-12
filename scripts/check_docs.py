from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
PORTFOLIO_MANIFEST = ROOT / "docs" / "portfolio-manifest.json"
REPOSITORY_METADATA_MANIFEST = ROOT / "config" / "repository-metadata.json"
REPO_NAME_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+$")
TOPIC_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,49}$")
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "cv-project-bullets.md",
    ROOT / "docs" / "linkedin-featured-copy.md",
    ROOT / "docs" / "recruiter-reading-paths.md",
    ROOT / "docs" / "30-second-project-summaries.md",
    ROOT / "docs" / "capability-matrix.md",
    ROOT / "docs" / "cv-headline-about.md",
    ROOT / "docs" / "interview-explanations.md",
    ROOT / "docs" / "outreach-snippets.md",
    ROOT / "docs" / "site-sync-brief.md",
    ROOT / "docs" / "portfolio-manifest.json",
    ROOT / "docs" / "ops-copilot-note.md",
    ROOT / "docs" / "lead-case-study-comparison.md",
]
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def should_skip_link(target: str) -> bool:
    return (
        target.startswith(("http://", "https://", "mailto:", "#"))
        or target.startswith("javascript:")
    )


def validate_required_files() -> list[str]:
    errors = []
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")
    return errors


def validate_markdown_links() -> list[str]:
    errors = []
    for markdown_file in MARKDOWN_FILES:
        content = markdown_file.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(content):
            target = raw_target.strip()
            if should_skip_link(target):
                continue
            clean_target = target.split("#", 1)[0]
            resolved = (markdown_file.parent / clean_target).resolve()
            if not resolved.exists():
                rel_file = markdown_file.relative_to(ROOT)
                errors.append(f"Broken relative link in {rel_file}: {target}")
    return errors


def validate_manifest() -> list[str]:
    errors = []
    try:
        manifest = json.loads(PORTFOLIO_MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"Invalid portfolio manifest JSON: {exc}"]

    required_top_level_keys = {
        "positioning",
        "default_reading_path",
        "lead_projects",
        "supporting_evidence",
        "reading_paths",
        "application_pack",
        "site_sync",
    }
    missing = sorted(required_top_level_keys - set(manifest.keys()))
    if missing:
        errors.append(f"Portfolio manifest missing keys: {', '.join(missing)}")

    lead_projects = manifest.get("lead_projects", [])
    if len(lead_projects) < 3:
        errors.append("Portfolio manifest must contain at least three lead projects.")
    else:
        for index, project in enumerate(lead_projects, start=1):
            for key in ("repo", "role", "repo_url", "demo_url", "thesis", "metrics"):
                if key not in project:
                    errors.append(f"Lead project #{index} missing key: {key}")
    return errors



def validate_repository_metadata() -> list[str]:
    """Check the presentation manifest offline, without API calls or runner minutes."""
    errors = []
    try:
        manifest = json.loads(REPOSITORY_METADATA_MANIFEST.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"Invalid repository metadata manifest: {exc}"]

    if manifest.get("owner") != "senanurcetin":
        errors.append("Repository metadata manifest has an unexpected owner.")
    entries = manifest.get("repositories")
    if not isinstance(entries, list) or not entries:
        return errors + ["Repository metadata manifest must have a nonempty repositories list."]

    names = set()
    for index, entry in enumerate(entries, start=1):
        if not isinstance(entry, dict):
            errors.append(f"Repository entry #{index} is not an object.")
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not REPO_NAME_PATTERN.fullmatch(name):
            errors.append(f"Repository entry #{index} has an invalid name.")
            continue
        if name in names:
            errors.append(f"Duplicate repository metadata entry: {name}")
        names.add(name)

        topics = entry.get("topics")
        if topics is not None:
            if not isinstance(topics, list) or len(topics) > 20 or any(
                not isinstance(t, str) or not TOPIC_PATTERN.fullmatch(t) for t in topics
            ) or len(set(topics)) != len(topics):
                errors.append(f"Invalid or duplicate Topics for {name}")

        branch = entry.get("default_branch", "main")
        if not isinstance(branch, str) or not branch or not re.fullmatch(
            r"[A-Za-z0-9._/-]+", branch
        ) or branch.startswith(("/", "-")) or ".." in branch:
            errors.append(f"Invalid default_branch for {name}")

        preview = entry.get("social_preview")
        if preview is not None:
            if not isinstance(preview, str) or preview.startswith("/") or (
                ".." in Path(preview).parts
            ) or Path(preview).suffix.lower() not in {".png", ".jpg", ".jpeg"}:
                errors.append(f"Unsafe or unsupported social_preview path for {name}")

        homepage = entry.get("homepage")
        if homepage is not None and (
            not isinstance(homepage, str) or not homepage.startswith("https://")
        ):
            errors.append(f"Invalid homepage URL for {name}")
    return errors


def validate_circleci_inventory() -> list[str]:
    """Run offline CI status classifier tests within the existing docs job."""
    errors = []
    path = ROOT / "config" / "circleci-projects.json"
    try:
        projects = json.loads(path.read_text(encoding="utf-8"))["projects"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f"CircleCI inventory cannot be read: {exc}"]
    if not isinstance(projects, list) or len(projects) < 12:
        errors.append("CircleCI inventory must include the 12 established projects.")
        return errors
    seen = set()
    for project in projects:
        repo = project.get("repo", "")
        contexts = project.get("contexts", [])
        if not re.fullmatch(r"senanurcetin/[A-Za-z0-9_.-]+", repo):
            errors.append(f"Invalid CircleCI repository: {repo}")
        if repo in seen:
            errors.append(f"Duplicate CircleCI repository: {repo}")
        seen.add(repo)
        if not contexts or not isinstance(contexts, list) or (
            any(not isinstance(x, str) or not x.startswith("ci/circleci: ") for x in contexts)
            or len(contexts) != len(set(contexts))
        ):
            errors.append(f"Invalid CircleCI status contexts for {repo}")
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(ROOT / "tests"), pattern="test_circleci_health.py"
    )
    if not unittest.TextTestRunner(verbosity=0).run(suite).wasSuccessful():
        errors.append("CircleCI classifier unit tests failed.")
    return errors


def main() -> int:
    errors = []
    errors.extend(validate_required_files())
    errors.extend(validate_markdown_links())
    errors.extend(validate_manifest())
    errors.extend(validate_repository_metadata())
    errors.extend(validate_circleci_inventory())
    if errors:
        for error in errors:
            print(error)
        return 1
    print("Docs check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
