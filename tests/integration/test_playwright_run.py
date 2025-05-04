import sys
import os
import time
import json
import pytest

# Add the src folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from run_playwright_tests import run_playwright_tests

REPORT_PATH = "playwright-report/test-results.json"

# Fixture to run Playwright tests and load the JSON report
@pytest.fixture(scope="session")
def run_and_parse_playwright():
    returncode, stdout, stderr = run_playwright_tests()

    # Ensure tests ran successfully
    assert returncode == 0, f"Playwright tests failed with returncode {returncode}.\n{stderr}"

    # Await to ensure report file is written
    for _ in range(10):
        if os.path.exists(REPORT_PATH):
            break
        time.sleep(1)
    else:
        raise FileNotFoundError(f"{REPORT_PATH} not found after waiting.")

    # Load and return JSON test results
    try:
        with open(REPORT_PATH, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to decode JSON report: {e}")

# Test to assert all Playwright tests passed
def test_all_playwright_tests_passed(run_and_parse_playwright):
    failed_tests = [
        test for test in run_and_parse_playwright.get("suites", [])
        if test.get("status") == "failed"
    ]
    assert len(failed_tests) == 0, f"Found failed tests: {failed_tests}"
