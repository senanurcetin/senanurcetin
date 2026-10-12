"""Offline state-classification tests; require neither network nor credentials."""
import importlib.util
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "circleci_health.py"
spec = importlib.util.spec_from_file_location("circleci_health", MODULE_PATH)
health = importlib.util.module_from_spec(spec)
spec.loader.exec_module(health)

A = "ci/circleci: web-quality"
B = "ci/circleci: analysis-quality"


class CircleCIStateTest(unittest.TestCase):
    def test_all_required_passed(self):
        self.assertEqual(health.classify("change", [
            {"context": A, "state": "success"}, {"context": B, "state": "success"},
        ], [A, B]), ("PASSED", []))

    def test_partial_success_not_green(self):
        self.assertEqual(health.classify("change", [
            {"context": A, "state": "success"},
        ], [A, B]), ("MISSING", [B]))

    def test_vercel_failure_does_not_mask_circleci(self):
        self.assertEqual(health.classify("change", [
            {"context": "Vercel", "state": "failure"},
            {"context": A, "state": "pending"},
            {"context": B, "state": "success"},
        ], [A, B]), ("PENDING", []))

    def test_circleci_failure_not_overridden_by_pending(self):
        self.assertEqual(health.classify("change", [
            {"context": A, "state": "failure"},
            {"context": B, "state": "pending"},
        ], [A, B]), ("FAILED", []))

    def test_explicit_skip_is_not_pass(self):
        self.assertEqual(health.classify("docs [skip ci]", [], [A]), ("SKIPPED", [A]))
        self.assertEqual(health.classify("docs [ci skip]", [], [A]), ("SKIPPED", [A]))

    def test_missing_status_not_skipped(self):
        self.assertEqual(health.classify("docs update", [], [A]), ("MISSING", [A]))

    def test_newest_status_wins(self):
        self.assertEqual(health.classify("code", [
            {"context": A, "state": "success"},
            {"context": A, "state": "failure"},
        ], [A]), ("PASSED", []))


if __name__ == "__main__":
    unittest.main()
