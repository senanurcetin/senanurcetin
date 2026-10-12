#!/usr/bin/env python3
"""Prepare honest 1280x640 GitHub Social Preview PNGs from existing project screenshots.

Generated images are local candidates; the GitHub Settings upload is manual.
Requires Pillow: python -m pip install Pillow
"""
from __future__ import annotations

import argparse
import json
import re
from io import BytesIO
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import urlopen

try:
    from PIL import Image, ImageDraw, ImageFont, ImageOps
except ImportError as exc:
    raise SystemExit("Install Pillow: python -m pip install Pillow") from exc

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "repository-metadata.json"
RESAMPLE = Image.Resampling.LANCZOS


def font(size: int):
    for name in ("DejaVuSans-Bold.ttf", "Arial.ttf", "DejaVuSans.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def card(title: str, screenshot: Image.Image) -> Image.Image:
    image = Image.new("RGB", (1280, 640), (12, 21, 37))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((30, 28, 1250, 612), radius=32, outline=(62, 83, 115), width=3)
    draw.rectangle((46, 84, 54, 174), fill=(59, 176, 191))
    draw.text((78, 92), "PROJECT", fill=(100, 210, 222), font=font(28))
    words = title.replace("-", " ").split()
    lines = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) > 19 and current:
            lines.append(current)
            current = word
        else:
            current = candidate
    if current:
        lines.append(current)
    for i, line in enumerate(lines[:4]):
        draw.text((78, 148 + 57 * i), line, fill=(246, 248, 252), font=font(36))
    draw.text((78, 480), "AUTHENTIC", fill=(100, 210, 222), font=font(22))
    draw.text((78, 510), "REPOSITORY VISUAL", fill=(180, 193, 209), font=font(18))
    draw.text((78, 563), "See README for evidence", fill=(153, 167, 185), font=font(17))

    draw.rounded_rectangle((457, 68, 1210, 561), radius=18, fill=(232, 237, 245))
    actual = ImageOps.exif_transpose(screenshot).convert("RGB")
    actual.thumbnail((731, 472), RESAMPLE)
    x = 468 + (731 - actual.width) // 2
    y = 79 + (472 - actual.height) // 2
    image.paste(actual, (x, y))
    return image


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", action="append", default=[], help="Limit to these repository names")
    parser.add_argument("--output", type=Path, default=Path("social-previews"))
    parser.add_argument("--write", action="store_true", help="Download genuine screenshots and write PNG files")
    args = parser.parse_args()

    config = json.loads(MANIFEST.read_text(encoding="utf-8"))
    owner = config["owner"]
    available = {entry["name"] for entry in config["repositories"]}
    if set(args.repo) - available:
        parser.error("Unknown repository name in --repo")
    selected = [e for e in config["repositories"] if not args.repo or e["name"] in args.repo]
    generated = 0
    for entry in selected:
        name = entry["name"]
        source = entry.get("social_preview")
        if not source:
            print(f"SKIP {name}: no verified authentic screenshot")
            continue
        if not re.fullmatch(r"[a-zA-Z0-9_.-]+", name):
            parser.error(f"Invalid repository name: {name}")
        url = f"https://raw.githubusercontent.com/{owner}/{name}/main/{quote(source, safe='/')}"
        dest = args.output / f"{name}.png"
        print(f"{'WRITE' if args.write else 'PLAN '} {dest} from {url}")
        if not args.write:
            continue
        if dest.exists():
            print("  existing candidate preserved; delete or move it explicitly to regenerate")
            continue
        try:
            with urlopen(url, timeout=25) as response:
                data = response.read(16_000_001)
            if len(data) > 16_000_000:
                raise RuntimeError("Image is unexpectedly large")
            with Image.open(BytesIO(data)) as screenshot:
                result = card(name, screenshot)
            dest.parent.mkdir(parents=True, exist_ok=True)
            result.save(dest, "PNG", optimize=True)
            generated += 1
        except (OSError, HTTPError, URLError, RuntimeError) as exc:
            print(f"  ERROR: {exc}; no placeholder/fake screenshot produced")
    print(f"Prepared {generated} PNG social-preview candidates.")
    if not args.write:
        print("No images written. Add --write to generate local candidates.")


if __name__ == "__main__":
    main()
