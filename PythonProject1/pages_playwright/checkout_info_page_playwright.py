# pages_playwright/checkout_info_page_playwright.py

from .base_page_playwright import BasePage

class CheckoutInfoPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name_input = "input[data-test='firstName']"
        self.last_name_input = "input[data-test='lastName']"
        self.postal_code_input = "input[data-test='postalCode']"
        self.continue_button = "input[data-test='continue']"

    async def enter_info(self, first_name: str, last_name: str, zip_code: str):
        await self.wait_and_fill(self.first_name_input, first_name)
        await self.wait_and_fill(self.last_name_input, last_name)
        await self.wait_and_fill(self.postal_code_input, zip_code)
        await self.wait_and_click(self.continue_button)
