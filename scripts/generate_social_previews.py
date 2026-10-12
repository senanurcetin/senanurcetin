#!/usr/bin/env python3
"""Build genuine, screenshot-led GitHub Social Previews (1280x640).

Uses ONLY the screenshots referenced in config/repository-metadata.json.
Colors and typography follow nexus-web-v2: paper, ink, blue, and navy.
No charts, numerical claims, app screens, or UI content are invented.

Dry run by default. Use --write --replace to regenerate older candidate files.
Social Preview settings on GitHub must be updated separately.
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
    raise SystemExit("Pillow is required: python -m pip install Pillow") from exc

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "config" / "repository-metadata.json"
W, H = 1280, 640
R = Image.Resampling.LANCZOS

# Verified topic labels, without invented scores or production claims.
BRIEFS = {
    "ms-capital-market-forecasting": (
        "MS Capital\nForecasting", "Financial ML research",
        ("BigQuery", "LightGBM", "Walk-forward"),
    ),
    "ieee-fraud-detection-analytics": (
        "Fraud Risk\nIntelligence", "Fraud analytics & model evaluation",
        ("Risk analytics", "LightGBM", "dbt"),
    ),
    "smart-factory-app": (
        "Smart Factory\nAnalytics", "Predictive maintenance & RUL",
        ("Industry 4.0", "ML", "Flask"),
    ),
    "visual-qc-project": (
        "Visual Quality\nControl", "Computer vision & defect analysis",
        ("Computer vision", "Quality control"),
    ),
    "ot-sentinel": (
        "OT-Sentinel", "Industrial anomaly detection",
        ("OT security", "Detection", "Next.js"),
    ),
    "E-commerce": (
        "E-commerce\nAnalytics", "Warehouse modeling & Power BI",
        ("dbt", "BigQuery", "Power BI"),
    ),
    "football-player-performance-analysis": (
        "Football\nAnalytics", "Player performance & market modeling",
        ("BigQuery", "dbt", "Power BI"),
    ),
    "Ops-Copilot": (
        "Ops-Copilot", "Document-grounded operator support",
        ("Industrial AI", "RAG", "Next.js"),
    ),
    "PlantLog-MERN": (
        "PlantLog", "Industrial maintenance logbook",
        ("MERN", "Maintenance", "Operations"),
    ),
    "ChemView": (
        "ChemView", "HMI & digital twin simulation",
        ("HMI", "Digital twin", "React"),
    ),
}

PAPER = "#f7f8fa"
WHITE = "#ffffff"
NAVY = "#061524"
INK = "#091625"
BLUE = "#0572a8"
LINE = "#d9e1e9"
MUTED = "#66717f"


def load_font(size: int, serif: bool = False, bold: bool = False):
    if serif:
        choices = [
            "C:/Windows/Fonts/georgia.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
            "Georgia.ttf", "DejaVuSerif.ttf",
        ]
    elif bold:
        choices = [
            "C:/Windows/Fonts/seguisb.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
            "DejaVuSans-Bold.ttf",
        ]
    else:
        choices = [
            "C:/Windows/Fonts/segoeui.ttf",
            "C:/Windows/Fonts/arial.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            "DejaVuSans.ttf",
        ]
    for path in choices:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def text_width(draw, text, font):
    bb = draw.textbbox((0, 0), text, font=font)
    return bb[2] - bb[0]


def fit_single_line(draw, text, max_width, base=25, min_size=17):
    for size in range(base, min_size - 1, -1):
        f = load_font(size)
        if text_width(draw, text, f) <= max_width:
            return f
    return load_font(min_size)


def title_font(draw, lines):
    for size in range(56, 37, -1):
        f = load_font(size, serif=True)
        if all(text_width(draw, line, f) <= 392 for line in lines):
            return f
    return load_font(38, serif=True)


def rounded_crop_mask(size, radius):
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255
    )
    return mask


def render(screenshot, entry, variant):
    name = entry["name"]
    title, subtitle, tags = BRIEFS.get(
        name,
        (name.replace("-", " ").title(), "Project case study", tuple()),
    )
    dark = variant == "dark"
    background = NAVY if dark else PAPER
    fg = WHITE if dark else INK
    secondary = "#b6c9d9" if dark else MUTED
    thin = "#27425b" if dark else LINE
    accent = "#77c7f2" if dark else BLUE

    canvas = Image.new("RGB", (W, H), background)
    d = ImageDraw.Draw(canvas)

    # Restrained editorial accents that match the website theme, not green.
    d.rectangle((0, 0, 9, H), fill=BLUE)
    d.line((40, 84, 422, 84), fill=thin, width=2)
    d.rectangle((43, 56, 81, 61), fill=accent)
    d.text(
        (92, 44), "PROJECT  /  CASE STUDY",
        font=load_font(18, bold=True), fill=accent,
    )

    lines = title.split("\n")
    font = title_font(d, lines)
    y = 142 if len(lines) <= 2 else 119
    for line in lines[:3]:
        d.text((43, y), line, font=font, fill=fg, stroke_width=0)
        y += 72

    subtitle_font = fit_single_line(d, subtitle, 390, base=22)
    d.text((44, y + 23), subtitle, fill=secondary, font=subtitle_font)

    # Technology chips: maximum three, never substitute invented metrics.
    tx, ty = 43, y + 89
    for tag in tags[:3]:
        f = load_font(17, bold=True)
        chip_w = min(185, text_width(d, tag, f) + 26)
        if tx + chip_w > 423:
            break
        d.rounded_rectangle(
            (tx, ty, tx + chip_w, ty + 38), radius=13,
            fill="#142e46" if dark else "#e7f2fa",
            outline="#315471" if dark else "#c8dce9",
            width=1,
        )
        d.text((tx + 13, ty + 8), tag, font=f, fill="#d5ebff" if dark else "#174566")
        tx += chip_w + 9

    d.line((43, 538, 422, 538), fill=thin, width=2)
    d.text((44, 556), "SENANUR CETIN  /  GITHUB",
           fill=secondary, font=load_font(16, bold=True))
    d.text((44, 584), "Fork-based analysis" if entry.get("fork") else "Independent project",
           fill=accent, font=load_font(16))

    # Screenshot takes >60% of the frame. No fake monitor shell or mock figures.
    x1, y1, x2, y2 = 458, 45, 1245, 592
    d.rounded_rectangle((x1 + 7, y1 + 10, x2 + 7, y2 + 10),
                        radius=21, fill="#d9e2eb" if not dark else "#0d2a41")
    d.rounded_rectangle((x1, y1, x2, y2),
                        radius=21, fill=WHITE if not dark else "#102638",
                        outline=LINE if not dark else "#345066", width=2)
    # Small browser-chrome band; no fabricated controls or analytical widgets.
    chrome_y = y1 + 43
    d.line((x1, chrome_y, x2, chrome_y),
           fill=LINE if not dark else "#345066", width=2)
    for i, c in enumerate(("#b7c5d3", "#91adbe", "#5e99bc")):
        d.ellipse((x1 + 17 + i * 20, y1 + 16, x1 + 25 + i * 20, y1 + 24), fill=c)
    d.text((x1 + 110, y1 + 12), "SOURCE SCREENSHOT",
           fill="#718496" if not dark else "#b1c6d3",
           font=load_font(15, bold=True))

    # Preserve entire screenshot; never crop analytics, source labels, or legends.
    view_w, view_h = x2 - x1 - 32, y2 - chrome_y - 38
    original = ImageOps.exif_transpose(screenshot).convert("RGB")
    thumb = ImageOps.contain(original, (view_w, view_h), method=R)
    ox = x1 + 16 + (view_w - thumb.width) // 2
    oy = chrome_y + 12 + (view_h - thumb.height) // 2
    canvas.paste(thumb, (ox, oy))
    d.rectangle((x1 + 16, y2 - 18, x1 + 67, y2 - 15), fill=BLUE)
    return canvas


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", action="append", default=[],
                        help="Only generate for these repos; may repeat")
    parser.add_argument("--output", type=Path, default=Path("social-previews"))
    parser.add_argument("--variant", choices=("light", "dark", "both"), default="light")
    parser.add_argument("--write", action="store_true", help="Download screenshot and create previews")
    parser.add_argument("--replace", action="store_true",
                        help="Replace OLD local preview files; requires --write")
    parser.add_argument("--contact-sheet", action="store_true",
                        help="Build an overview JPEG from the generated PNGs")
    args = parser.parse_args()
    if args.replace and not args.write:
        parser.error("--replace requires --write")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    owner = manifest["owner"]
    records = manifest["repositories"]
    available = {e["name"] for e in records}
    if set(args.repo) - available:
        parser.error(f"Unknown repo: {', '.join(sorted(set(args.repo) - available))}")

    entries = [e for e in records if not args.repo or e["name"] in args.repo]
    variants = ("light", "dark") if args.variant == "both" else (args.variant,)
    written = 0
    generated = []

    for entry in entries:
        name, source = entry["name"], entry.get("social_preview")
        if not source:
            print(f"SKIP  {name}: no verified image")
            continue
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", name):
            parser.error(f"Unsafe repo name: {name}")
        url = (f"https://raw.githubusercontent.com/{owner}/{name}/{entry.get('default_branch', 'main')}/"
               f"{quote(source, safe='/')}")
        images = [(v, args.output / f"{name}{'-dark' if v == 'dark' else ''}.png")
                  for v in variants]
        print(f"{'WRITE' if args.write else 'PLAN '} {name}: {source}")
        if not args.write:
            continue
        pending = [(v, p) for v, p in images if args.replace or not p.exists()]
        if not pending:
            print("  Existing candidates preserved. Use --replace for redesign.")
            generated.extend(p for _, p in images if p.exists())
            continue
        try:
            with urlopen(url, timeout=25) as response:
                raw = response.read(16_000_001)
            if len(raw) > 16_000_000:
                raise ValueError("Unexpectedly large screenshot")
            with Image.open(BytesIO(raw)) as source_image:
                source_image.load()
                for variant, target in pending:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    rendered = render(source_image, entry, variant)
                    rendered.save(target, "PNG", optimize=True)
                    generated.append(target)
                    written += 1
                    print(f"  Created {target} ({target.stat().st_size:,} bytes)")
        except (OSError, HTTPError, URLError, ValueError) as exc:
            print(f"  ERROR downloading/decoding screenshot: {exc}")
            print("  No fake placeholder was generated.")

    if args.contact_sheet and args.write:
        candidates = sorted(set(generated + [
            p for e in entries for v in variants
            for p in [args.output / f"{e['name']}{'-dark' if v == 'dark' else ''}.png"]
            if p.exists()
        ]))
        if candidates:
            cell_w, cell_h, gap = 580, 290, 20
            rows = (len(candidates) + 1) // 2
            sheet = Image.new("RGB", (cell_w * 2 + gap * 3,
                                      rows * cell_h + gap * (rows + 1)), PAPER)
            for idx, path in enumerate(candidates):
                with Image.open(path) as cover:
                    thumb = cover.convert("RGB").resize((cell_w, cell_h), R)
                cx = gap + (idx % 2) * (cell_w + gap)
                cy = gap + (idx // 2) * (cell_h + gap)
                sheet.paste(thumb, (cx, cy))
            dest = args.output / "contact-sheet.jpg"
            sheet.save(dest, "JPEG", quality=88, optimize=True)
            print(f"Contact sheet: {dest}")
    print(f"Finished: {written} new screenshot-based 1280x640 PNG files.")
    if not args.write:
        print("No images changed. Add --write --replace to regenerate old previews.")


if __name__ == "__main__":
    main()
