import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

PASSWORD = "secret_sauce"  # public demo password shown on saucedemo.com


@pytest.mark.smoke
def test_standard_user_can_log_in(driver):
    LoginPage(driver).open().login("standard_user", PASSWORD)
    assert InventoryPage(driver).title() == "Products"


def test_locked_out_user_sees_error(driver):
    page = LoginPage(driver).open()
    page.login("locked_out_user", PASSWORD)
    assert "locked out" in page.error_text()


@pytest.mark.parametrize("user,pwd,msg", [
    ("", PASSWORD, "Username is required"),
    ("standard_user", "", "Password is required"),
    ("standard_user", "wrong", "do not match"),
])
def test_login_validation(driver, user, pwd, msg):
    page = LoginPage(driver).open()
    page.login(user, pwd)
    assert msg in page.error_text()
