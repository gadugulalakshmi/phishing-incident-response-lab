
import json
import subprocess
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = PROJECT_ROOT / "scripts" / "analyze-auth-log.py"
REPORT = PROJECT_ROOT / "reports" / "alerts.json"


class TestAuthenticationAnalyzer(unittest.TestCase):

    def test_analyzer_runs_successfully(self):
        result = subprocess.run(
            ["python3", str(SCRIPT)],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Authentication Log Analysis", result.stdout)
        self.assertIn("Successful logins: 3", result.stdout)
        self.assertIn("Failed logins: 1", result.stdout)
        self.assertIn("Repeated Failed Login Alerts", result.stdout)

    def test_json_report_is_generated(self):
        subprocess.run(
            ["python3", str(SCRIPT)],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )

        self.assertTrue(REPORT.exists(), "JSON report was not generated")

        with REPORT.open("r", encoding="utf-8") as file:
            report = json.load(file)

        self.assertEqual(report["summary"]["successful_logins"], 3)
        self.assertEqual(report["summary"]["failed_logins"], 1)
        self.assertEqual(report["summary"]["alerts_generated"], 2)
        self.assertEqual(len(report["alerts"]), 2)


if __name__ == "__main__":
    unittest.main()

