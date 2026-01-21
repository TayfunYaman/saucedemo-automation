# SauceDemo Test Automation Project
![CI](https://github.com/TayfunYaman/saucedemo-automation/actions/workflows/ci.yml/badge.svg)

## Tech Stack
- Python 3.10
- Selenium WebDriver
- Pytest
- Pytest-HTML
- Page Object Model (POM)

## Project Structure
- pages/: Page Object classes
- tests/: Test cases
- conftest.py: Fixtures
- pytest.ini: Pytest configuration

## How to Run Tests
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
