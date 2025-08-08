from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductsPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")

    def verify_products_title(self):
        return self.get_text(self.TITLE) == "Products"

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)
