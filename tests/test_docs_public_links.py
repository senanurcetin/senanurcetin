"""Public link audits should distinguish signed-in account controls from public 404s."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_public_links  # noqa: E402


class AuthenticatedControlLinkTests(unittest.TestCase):
    def test_github_repo_settings_do_not_receive_public_http_probe(self) -> None:
        item = ("https://github.com/senanurcetin/visual-qc-project/settings", ["docs/guide.md"])
        with patch.object(audit_public_links, "request_status") as request:
            result = audit_public_links.audit(item, timeout=1.0)
        request.assert_not_called()
        self.assertEqual("auth-required", result["verdict"])
        self.assertIsNone(result["status"])
        self.assertEqual(item[0], result["destination"])

    def test_nested_settings_page_is_an_authenticated_control(self) -> None:
        url = "https://github.com/owner/repo/settings/pages?tab=custom"
        with patch.object(audit_public_links, "request_status") as request:
            result = audit_public_links.audit((url, []), timeout=1.0)
        request.assert_not_called()
        self.assertEqual("auth-required", result["verdict"])

    def test_public_repository_404_is_still_reported(self) -> None:
        url = "https://github.com/owner/repo/blob/main/README.md"
        with patch.object(
            audit_public_links, "request_status", return_value=(404, url)
        ) as request:
            result = audit_public_links.audit((url, []), timeout=1.0)
        self.assertEqual("candidate-broken", result["verdict"])
        self.assertEqual(2, request.call_count)  # HEAD then GET

    def test_lookalike_host_and_path_are_not_trusted(self) -> None:
        for url in (
            "https://evilgithub.com/owner/repo/settings",
            "https://github.com/owner/repo/settings-old",
        ):
            with self.subTest(url=url):
                with patch.object(
                    audit_public_links, "request_status", return_value=(404, url)
                ) as request:
                    result = audit_public_links.audit((url, []), timeout=1.0)
                self.assertEqual("candidate-broken", result["verdict"])
                self.assertEqual(2, request.call_count)


if __name__ == "__main__":
    unittest.main()
