from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutOverviewPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    FINISH_BUTTON = (By.ID, "finish")

    def is_overview_displayed(self):
        return self.get_text(self.TITLE) == "Checkout: Overview"

    def finish(self):
        self.click(self.FINISH_BUTTON)
