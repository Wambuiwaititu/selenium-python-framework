import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def inventory(driver):
    LoginPage(driver).open().login("standard_user", "secret_sauce")
    return InventoryPage(driver)


def test_six_products_listed(inventory):
    assert inventory.item_count() == 6


@pytest.mark.smoke
def test_add_two_items_updates_cart_badge(inventory):
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.add_to_cart("sauce-labs-bike-light")
    assert inventory.cart_count() == 2


def test_sort_price_low_to_high(inventory):
    inventory.sort_by("lohi")
    prices = inventory.prices()
    assert prices == sorted(prices)
