import subprocess
import os

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

    # Open HTML report locally, not in CI
    if result.returncode == 0 and os.environ.get("CI") != "true":
        subprocess.run(["npx", "playwright", "show-report"])

    return result.returncode, result.stdout, result.stderr
