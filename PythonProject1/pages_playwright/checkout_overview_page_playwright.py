# pages_playwright/checkout_overview_page_playwright.py

from .base_page_playwright import BasePage

class CheckoutOverviewPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title_selector = "span.title"
        self.finish_button = "button[data-test='finish']"

    async def verify_title(self) -> bool:
        await self.page.wait_for_selector(self.title_selector, state="visible")
        await self.highlight(self.title_selector)
        return await self.page.is_visible(self.title_selector)

    async def click_finish(self):
        await self.wait_and_click(self.finish_button)
