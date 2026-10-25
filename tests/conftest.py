import os
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--headed", action="store_true", help="run with a visible browser")


@pytest.fixture
def driver(request):
    opts = webdriver.ChromeOptions()
    if not request.config.getoption("--headed"):
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1280,900")
    opts.add_argument("--no-sandbox")
    drv = webdriver.Chrome(options=opts)
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot into reports/ when a test fails."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed and "driver" in item.funcargs:
        os.makedirs("reports", exist_ok=True)
        item.funcargs["driver"].save_screenshot(f"reports/{item.name}.png")
