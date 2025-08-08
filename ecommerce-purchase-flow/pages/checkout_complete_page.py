from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def verify_success(self):
        return self.get_text(self.COMPLETE_HEADER) == "Thank you for your order!"
