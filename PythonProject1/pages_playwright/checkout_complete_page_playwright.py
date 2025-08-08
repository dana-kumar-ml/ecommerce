# pages_playwright/checkout_complete_page_playwright.py

from .base_page_playwright import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.complete_header_selector = "h2.complete-header"

    async def verify_complete(self) -> bool:
        await self.page.wait_for_selector(self.complete_header_selector, state="visible")
        await self.highlight(self.complete_header_selector)
        return await self.page.is_visible(self.complete_header_selector)
