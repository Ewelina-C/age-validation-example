import subprocess
import os

REPORT_PATH = "playwright-report/test-results.json"

def run_playwright_tests():
    # Run Playwright tests with both JSON and HTML reporters
    result = subprocess.run(
        [
            "npx", "playwright", "test",
            "--reporter", "json,html",
        ],
        capture_output=True,
        text=True
    )

    # Only show report when not in CI (skip to avoid timeouts in GitHub Actions)
    if result.returncode == 0 and not os.environ.get("CI", "").lower() == "true":
        subprocess.run(["npx", "playwright", "show-report"])

    return result.returncode, result.stdout, result.stderr
