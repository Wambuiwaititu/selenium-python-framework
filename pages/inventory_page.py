from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "[data-test='title']")
    ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    CART_BADGE = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")
    SORT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    PRICES = (By.CSS_SELECTOR, "[data-test='inventory-item-price']")

    def title(self):
        return self.find(self.TITLE).text

    def item_count(self):
        self.find(self.ITEMS)
        return len(self.driver.find_elements(*self.ITEMS))

    def add_to_cart(self, slug):
        self.click((By.ID, f"add-to-cart-{slug}"))

    def cart_count(self):
        return int(self.find(self.CART_BADGE).text)

    def sort_by(self, value):
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.SORT)).select_by_value(value)

    def prices(self):
        return [float(p.text.lstrip("$")) for p in self.driver.find_elements(*self.PRICES)]
