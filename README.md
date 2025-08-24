# Airport Gap Test Framework

## Tests

**UI Tests (SauceDemo.com):**
- Verify inventory page displays 6 items
- Add item to cart and verify badge shows 1

**API Tests (Airport Gap):**
- Verify API returns exactly 30 airports
- Verify specific airports are present (Akureyri, St. Anthony, CFB Bagotville)
- Verify distance between KIX-NRT airports > 400 km

## Installation

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
# Quick start (all tests once)
python run_tests.py

# All tests with pytest
pytest tests/ -v

# API tests only
pytest tests/api/ -m api -v

# UI tests only  
pytest tests/ui/ -m ui -v

# UI tests in headless mode
pytest tests/ui/ -m ui --headless -v

# Generate Allure report
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## Requirements

- Python 3.10+
- Chrome browser
- All Python dependencies in requirements.txt
