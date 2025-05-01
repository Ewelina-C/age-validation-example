# age-validation-example

This repository demonstrates a simple web-based age validation system using HTML, JavaScript, and Playwright for end-to-end testing. It includes a form where users can enter their age, with validation that ensures the age falls within a specified range.

## Features

- Input validation for age with minimum and maximum age constraints
- Playwright-based end-to-end tests for validation
- Pytest integration for automated testing

## Project Structure

- `index.html`: The main HTML file containing the form for age validation.
- `playwright-report/`: The directory where Playwright test results (HTML and JSON) are stored.
- `src/`: Contains Python scripts for running the Playwright tests.
- `tests/`: The folder where Playwright test scripts are stored.
- `playwright.config.ts`: Playwright configuration file.
- `package.json`: Contains the dependencies and scripts for running Playwright tests.
- `.github/workflows/playwright-report.yml`: GitHub Actions configuration for continuous integration.

## Getting Started

### Prerequisites

- Python 3.x
- Node.js
- Playwright
- Pytest for running tests

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Ewelina-C/age-validation-example.git
cd age-validation-example
```

2. Set up Python environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
pip install -r requirements.txt
```

3. Install Node.js dependencies

```bash
npm install
```

4. Install Playwright

```bash
npx playwright install
```

5. Run the tests

```bash
python src/run_playwright_tests.py
```

6. View the report

Open `playwright-report/index.html` in your browser to see the test results.



## GitHub Actions

This repository is set up to automatically run Playwright tests using GitHub Actions. The results are saved in the `playwright-report/` directory.


## Testing Age Validation

The local `index.html` page contains a form that asks for a user’s age. It validates that the input is within the specified range. If the age is invalid (either too low or too high), the user is prompted to enter a valid age.


## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.
