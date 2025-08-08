# pages_playwright/base_page_playwright.py

class BasePage:
    def __init__(self, page):
        self.page = page

    async def wait_and_click(self, selector: str):
        await self.page.wait_for_selector(selector, state="visible")
        await self.highlight(selector)
        await self.page.click(selector)

    async def wait_and_fill(self, selector: str, value: str):
        await self.page.wait_for_selector(selector, state="visible")
        await self.page.fill(selector, value)

    async def get_text(self, selector: str) -> str:
        await self.page.wait_for_selector(selector, state="visible")
        return await self.page.text_content(selector)

    async def is_visible(self, selector: str) -> bool:
        await self.page.wait_for_selector(selector, state="visible")
        return await self.page.is_visible(selector)

    async def highlight(self, selector: str):
        # Add a red border for 1 second for visibility
        await self.page.eval_on_selector(
            selector,
            """el => {
                el.style.border = '2px solid red';
                setTimeout(() => el.style.border = '', 1000);
            }"""
        )

    async def take_screenshot(self, path: str):
        await self.page.screenshot(path=path)
