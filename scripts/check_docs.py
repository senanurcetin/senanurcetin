from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_FILES = [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "cv-project-bullets.md",
    ROOT / "docs" / "linkedin-featured-copy.md",
    ROOT / "docs" / "recruiter-reading-paths.md",
    ROOT / "docs" / "30-second-project-summaries.md",
    ROOT / "docs" / "capability-matrix.md",
    ROOT / "docs" / "interview-explanations.md",
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


def main() -> int:
    errors = []
    errors.extend(validate_required_files())
    errors.extend(validate_markdown_links())
    if errors:
        for error in errors:
            print(error)
        return 1
    print("Docs check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
