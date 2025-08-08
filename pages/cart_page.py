from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def verify_item(self, expected_name):
        return self.get_text(self.ITEM_NAME) == expected_name

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
