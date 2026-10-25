# Selenium Python Framework

A small, clean **pytest + Selenium** UI test framework using the page-object model, run against the public practice site [saucedemo.com](https://www.saucedemo.com).

## Stack
Python 3.11+, Selenium 4 (Selenium Manager downloads the driver automatically), pytest, pytest-html, GitHub Actions

## Features
- Page objects (`pages/`) with explicit waits in a shared `BasePage`
- `driver` fixture: headless Chrome by default, `--headed` to watch
- Self-contained HTML report at `reports/report.html`
- Screenshot saved to `reports/` when a test fails
- `smoke` marker for quick critical-path runs
- Parametrised negative login tests

## Run it
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest                 # all tests + HTML report
pytest -m smoke        # smoke only
pytest --headed        # visible browser
```
Needs Google Chrome installed.

## Sample output
```
tests/test_inventory.py ...      [ 37%]
tests/test_login.py .....        [100%]
- Generated html report: reports/report.html -
8 passed in 9.21s
```

## Layout
```
pages/        BasePage, LoginPage, InventoryPage
tests/        conftest.py (fixtures, hooks), test_login.py, test_inventory.py
pytest.ini    report + marker config
```
The credentials in the tests are the public demo accounts published on saucedemo.com.
