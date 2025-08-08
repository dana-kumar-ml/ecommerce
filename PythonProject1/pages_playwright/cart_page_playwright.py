# pages_playwright/cart_page_playwright.py

from .base_page_playwright import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.item_name_selector = ".inventory_item_name"
        self.checkout_button = "#checkout"

    async def verify_item(self, expected_name: str) -> bool:
        await self.page.wait_for_selector(self.item_name_selector, state="visible")
        actual_name = await self.get_text(self.item_name_selector)
        return actual_name == expected_name

    async def click_checkout(self):
        await self.wait_and_click(self.checkout_button)
