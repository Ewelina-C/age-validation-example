import sys
import os

# Add the src folder to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Debug print to check the Python path
print(f"Current Python Path: {sys.path}")

# Now import the function from the correct location
from run_playwright_tests import run_playwright_tests


import pytest
import json
from run_playwright_tests import run_playwright_tests

REPORT_PATH = "playwright-report/test-results.json"

# Fixture to run Playwright tests and load the JSON report
@pytest.fixture(scope="session")
def run_and_parse_playwright():
    returncode, stdout, stderr = run_playwright_tests()
    
    # Ensure tests ran successfully
    assert returncode == 0, f"Playwright tests failed with returncode {returncode}.\n{stderr}"

    # Load and return the JSON test results
    with open(REPORT_PATH, 'r') as file:
        return json.load(file)

# Example test checking if Playwright tests passed
def test_all_playwright_tests_passed(run_and_parse_playwright):
    # Check if any tests failed
    failed_tests = [test for test in run_and_parse_playwright["suites"] if test.get("status") == "failed"]
    
    assert len(failed_tests) == 0, f"Found failed tests: {failed_tests}"
