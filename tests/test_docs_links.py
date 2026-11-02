"""Offline regression tests for profile documentation link verification."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_docs  # noqa: E402


class DocumentationLinksTests(unittest.TestCase):
    def test_nested_docs_are_included(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text("# Profile", encoding="utf-8")
            nested = root / "docs" / "benchmarks" / "report.md"
            nested.parent.mkdir(parents=True)
            nested.write_text("[missing](missing.png)", encoding="utf-8")
            with patch.object(check_docs, "ROOT", root):
                self.assertIn(nested, check_docs.discover_markdown_files())

    def test_missing_link_in_nested_docs_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text("# Profile", encoding="utf-8")
            nested = root / "docs" / "benchmarks" / "report.md"
            nested.parent.mkdir(parents=True)
            nested.write_text("[missing](missing.png)", encoding="utf-8")
            with patch.object(check_docs, "ROOT", root):
                self.assertEqual(
                    ["Broken relative link in docs/benchmarks/report.md: missing.png"],
                    check_docs.validate_markdown_links(),
                )

    def test_fenced_code_examples_are_not_real_links(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            markdown = root / "README.md"
            markdown.write_text(
                "# Example\n\n\x60\x60\x60md\n[example](not-an-asset.png)\n\x60\x60\x60\n",
                encoding="utf-8",
            )
            with patch.object(check_docs, "ROOT", root):
                self.assertEqual([], check_docs.validate_markdown_links())

    def test_percent_encoding_and_query_are_resolved(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "README.md").write_text(
                "[Evidence](docs/real%20figure.png?raw=1#figure)", encoding="utf-8"
            )
            (root / "docs").mkdir()
            (root / "docs" / "real figure.png").write_bytes(b"png")
            with patch.object(check_docs, "ROOT", root):
                self.assertEqual([], check_docs.validate_markdown_links())

    def test_relative_link_must_stay_within_repository(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            parent = Path(temporary)
            root = parent / "repo"
            root.mkdir()
            (root / "README.md").write_text("[outside](../outside.txt)", encoding="utf-8")
            (parent / "outside.txt").write_text("private", encoding="utf-8")
            with patch.object(check_docs, "ROOT", root):
                errors = check_docs.validate_markdown_links()
                self.assertEqual(
                    ["Relative link escapes repository in README.md: ../outside.txt"],
                    errors,
                )


if __name__ == "__main__":
    unittest.main()
