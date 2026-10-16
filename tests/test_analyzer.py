import subprocess
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = PROJECT_ROOT / "scripts" / "analyze-auth-log.py"


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


if __name__ == "__main__":
    unittest.main()
