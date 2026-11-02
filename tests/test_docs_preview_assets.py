"""Offline checks for the published, evidence-grounded GitHub preview cards."""

from __future__ import annotations

import json
import struct
import sys
import tempfile
import unittest
import zlib
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_docs  # noqa: E402


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return (
        struct.pack(">I", len(data))
        + kind
        + data
        + struct.pack(">I", zlib.crc32(kind + data))
    )


def sample_png(width: int = 1280, height: int = 640) -> bytes:
    header = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    rows = (b"\x00" + b"\x00" * (width * 3)) * height
    return (
        check_docs.PNG_SIGNATURE
        + png_chunk(b"IHDR", header)
        + png_chunk(b"IDAT", zlib.compress(rows, 1))
        + png_chunk(b"IEND", b"")
    )


class PreviewAssetTests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.cards = self.root / "assets" / "social-previews"
        self.cards.mkdir(parents=True)
        docs = self.root / "docs"
        docs.mkdir()
        self.guide = docs / "REPOSITORY_FINISHING_GUIDE.md"
        self.manifest = self.root / "config" / "repository-metadata.json"
        self.manifest.parent.mkdir()
        self.manifest.write_text(
            json.dumps({"repositories": [{"name": "demo", "social_preview": "docs/demo.png"}]}),
            encoding="utf-8",
        )
        self.guide.write_text(
            "[Demo](../assets/social-previews/demo.png)", encoding="utf-8"
        )
        (self.cards / "demo.png").write_bytes(sample_png())
        (self.cards / "contact-sheet.jpg").write_bytes(
            b"\xff\xd8" + (b"\x00" * 1024) + b"\xff\xd9"
        )
        root_patch = patch.object(check_docs, "ROOT", self.root)
        manifest_patch = patch.object(
            check_docs, "REPOSITORY_METADATA_MANIFEST", self.manifest
        )
        root_patch.start()
        manifest_patch.start()
        self.addCleanup(root_patch.stop)
        self.addCleanup(manifest_patch.stop)

    def test_valid_png_and_manifest_link_are_accepted(self) -> None:
        self.assertEqual([], check_docs.validate_social_preview_assets())

    def test_missing_linked_card_is_rejected(self) -> None:
        (self.cards / "demo.png").unlink()
        self.assertIn(
            "Social Preview linked but missing: demo.png",
            check_docs.validate_social_preview_assets(),
        )

    def test_png_checksum_corruption_is_rejected(self) -> None:
        card = self.cards / "demo.png"
        raw = bytearray(card.read_bytes())
        raw[30] ^= 1
        card.write_bytes(raw)
        self.assertTrue(
            any("checksum mismatch" in msg for msg in check_docs.validate_social_preview_assets())
        )

    def test_wrong_dimensions_are_rejected(self) -> None:
        (self.cards / "demo.png").write_bytes(sample_png(600, 640))
        self.assertTrue(
            any("unexpected dimensions" in msg for msg in check_docs.validate_social_preview_assets())
        )

    def test_unverified_card_is_rejected(self) -> None:
        (self.cards / "extra.png").write_bytes(sample_png())
        self.assertIn(
            "Social Preview lacks a verified source in metadata: extra.png",
            check_docs.validate_social_preview_assets(),
        )

    def test_missing_guide_link_is_rejected(self) -> None:
        self.guide.write_text("# No card reference", encoding="utf-8")
        self.assertIn(
            "Social Preview not linked from publishing guide: demo.png",
            check_docs.validate_social_preview_assets(),
        )

    def test_malformed_contact_sheet_is_rejected(self) -> None:
        (self.cards / "contact-sheet.jpg").write_bytes(b"bad")
        self.assertIn(
            "Social Preview contact-sheet.jpg is malformed",
            check_docs.validate_social_preview_assets(),
        )


if __name__ == "__main__":
    unittest.main()
