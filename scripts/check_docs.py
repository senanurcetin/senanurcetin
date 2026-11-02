from __future__ import annotations

import json
import re
import sys
import unittest
import zlib
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PORTFOLIO_MANIFEST = ROOT / "docs" / "portfolio-manifest.json"
REPOSITORY_METADATA_MANIFEST = ROOT / "config" / "repository-metadata.json"
REPO_NAME_PATTERN = re.compile(r"^[A-Za-z0-9_.-]+$")
TOPIC_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]{0,49}$")
REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "docs" / "capability-matrix.md",
    ROOT / "docs" / "site-sync-brief.md",
    ROOT / "docs" / "portfolio-manifest.json",
]
PREVIEW_LINK_PATTERN = re.compile(r"\]\(\.\./assets/social-previews/([A-Za-z0-9_.-]+\.png)\)")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
PREVIEW_WIDTH, PREVIEW_HEIGHT = 1280, 640
MAX_PREVIEW_BYTES = 8 * 1024 * 1024
LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FENCE_PATTERN = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING_PATTERN = re.compile(r"^ {0,3}#{1,6}[ \t]+(.+?)[ \t]*#*[ \t]*$", re.M)
EXPLICIT_ANCHOR_PATTERN = re.compile(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)["\x27]', re.I)


def discover_markdown_files() -> list[Path]:
    """Include nested docs (for example docs/benchmarks), not just top-level pages."""
    return [ROOT / "README.md", *sorted((ROOT / "docs").rglob("*.md"))]


def outside_fenced_code(content: str) -> str:
    lines = []
    fence: tuple[str, int] | None = None
    for line in content.splitlines(keepends=True):
        match = FENCE_PATTERN.match(line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
                continue
            if marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
                continue
        if fence is None:
            lines.append(line)
    return "".join(lines)


def should_skip_link(target: str) -> bool:
    # External schemes and application routes cannot be validated as local files.
    # A local #section fragment must be checked against Markdown headings.
    return target.startswith("/") or bool(urlsplit(target).scheme)


def markdown_anchors(path: Path) -> set[str]:
    """Collect GitHub-style heading IDs and explicit HTML anchors, offline."""
    contents = outside_fenced_code(path.read_text(encoding="utf-8"))
    anchors = set(EXPLICIT_ANCHOR_PATTERN.findall(contents))
    counts: dict[str, int] = {}
    for match in HEADING_PATTERN.finditer(contents):
        heading = re.sub(r"<[^>]*>", "", match.group(1))
        heading = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        heading = re.sub(r"\x60([^\x60]+)\x60", r"\1", heading)
        heading = re.sub(r"[*_~]", "", heading)
        slug = re.sub(r"\s", "-", re.sub(r"[^\w\- ]", "", heading.lower()).strip())
        if slug:
            count = counts.get(slug, 0)
            anchors.add(f"{slug}-{count}" if count else slug)
            counts[slug] = count + 1
    return anchors


def validate_required_files() -> list[str]:
    errors = []
    for path in REQUIRED_FILES:
        if not path.exists():
            errors.append(f"Missing required file: {path.relative_to(ROOT)}")
    return errors


def validate_markdown_links() -> list[str]:
    errors = []
    for markdown_file in discover_markdown_files():
        content = outside_fenced_code(markdown_file.read_text(encoding="utf-8"))
        for raw_target in LINK_PATTERN.findall(content):
            target = raw_target.strip()
            if should_skip_link(target):
                continue
            parsed = urlsplit(target)
            url_path = unquote(parsed.path)
            resolved = (markdown_file.parent / url_path).resolve() if url_path else markdown_file.resolve()
            rel_file = markdown_file.relative_to(ROOT).as_posix()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(f"Relative link escapes repository in {rel_file}: {target}")
                continue
            if not resolved.exists():
                errors.append(f"Broken relative link in {rel_file}: {target}")
            elif parsed.fragment and resolved.suffix.lower() in {".md", ".markdown"}:
                fragment = unquote(parsed.fragment)
                if fragment not in markdown_anchors(resolved):
                    errors.append(f"Broken Markdown anchor in {rel_file}: {target}")
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
        "technical_evidence",
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


def validate_png_card(path: Path) -> str | None:
    """Inspect PNG structure, CRCs and canvas size without third-party packages."""
    try:
        raw = path.read_bytes()
    except OSError as exc:
        return f"cannot read PNG: {exc}"
    if len(raw) > MAX_PREVIEW_BYTES:
        return "PNG exceeds the 8 MiB safety limit"
    if not raw.startswith(PNG_SIGNATURE):
        return "PNG signature is invalid"
    cursor = len(PNG_SIGNATURE)
    seen_header = False
    seen_data = False
    while cursor < len(raw):
        if cursor + 12 > len(raw):
            return "PNG chunk is truncated"
        length = int.from_bytes(raw[cursor:cursor + 4], "big")
        chunk_type = raw[cursor + 4:cursor + 8]
        end = cursor + 12 + length
        if end > len(raw):
            return "PNG chunk payload is truncated"
        payload = raw[cursor + 8:cursor + 8 + length]
        stored_crc = int.from_bytes(raw[cursor + 8 + length:end], "big")
        if zlib.crc32(chunk_type + payload) != stored_crc:
            return "PNG chunk checksum mismatch"
        if not seen_header:
            if chunk_type != b"IHDR" or length != 13:
                return "PNG must start with a 13-byte IHDR"
            width = int.from_bytes(payload[:4], "big")
            height = int.from_bytes(payload[4:8], "big")
            if (width, height) != (PREVIEW_WIDTH, PREVIEW_HEIGHT):
                return f"PNG has unexpected dimensions {width}x{height}"
            seen_header = True
        elif chunk_type == b"IDAT":
            seen_data = True
        elif chunk_type == b"IEND":
            if length != 0 or not seen_data or end != len(raw):
                return "PNG has invalid IEND, missing IDAT or trailing bytes"
            return None
        cursor = end
    return "PNG has no final IEND chunk"


def validate_social_preview_assets() -> list[str]:
    """Compare committed cards with the evidence manifest and public links."""
    errors = []
    directory = ROOT / "assets" / "social-previews"
    guide = ROOT / "docs" / "REPOSITORY_FINISHING_GUIDE.md"
    try:
        manifest = json.loads(REPOSITORY_METADATA_MANIFEST.read_text(encoding="utf-8"))
        guide_text = guide.read_text(encoding="utf-8")
        eligible = {
            entry["name"] + ".png"
            for entry in manifest["repositories"]
            if entry.get("social_preview")
        }
    except (OSError, KeyError, ValueError, TypeError) as exc:
        return [f"Preview asset inventory cannot be read: {exc}"]
    if not directory.is_dir():
        return ["Missing versioned Social Preview asset directory"]
    available = {path.name for path in directory.glob("*.png")}
    linked = set(PREVIEW_LINK_PATTERN.findall(guide_text))
    for name in sorted(eligible - available):
        errors.append(f"Social Preview expected by metadata but missing: {name}")
    for name in sorted(available - eligible):
        errors.append(f"Social Preview lacks a verified source in metadata: {name}")
    for name in sorted(linked - available):
        errors.append(f"Social Preview linked but missing: {name}")
    for name in sorted(available - linked):
        errors.append(f"Social Preview not linked from publishing guide: {name}")
    for name in sorted(available):
        reason = validate_png_card(directory / name)
        if reason:
            errors.append(f"Invalid Social Preview {name}: {reason}")
    contact = directory / "contact-sheet.jpg"
    if not contact.is_file():
        errors.append("Missing Social Preview contact-sheet.jpg")
    else:
        raw = contact.read_bytes()
        if len(raw) < 1000 or not raw.startswith(b"\xff\xd8") or not raw.endswith(b"\xff\xd9"):
            errors.append("Social Preview contact-sheet.jpg is malformed")
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


def validate_docs_regressions() -> list[str]:
    suite = unittest.defaultTestLoader.discover(
        start_dir=str(ROOT / "tests"), pattern="test_docs_*.py"
    )
    if not unittest.TextTestRunner(verbosity=0).run(suite).wasSuccessful():
        return ["Documentation link regression tests failed."]
    return []


def main() -> int:
    errors = []
    errors.extend(validate_required_files())
    errors.extend(validate_markdown_links())
    errors.extend(validate_social_preview_assets())
    errors.extend(validate_docs_regressions())
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
