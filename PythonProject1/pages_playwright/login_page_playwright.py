# pages_playwright/login_page_playwright.py

from .base_page_playwright import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"

    async def login(self, username: str, password: str):
        await self.wait_and_fill(self.username_input, username)
        await self.wait_and_fill(self.password_input, password)
        await self.wait_and_click(self.login_button)
