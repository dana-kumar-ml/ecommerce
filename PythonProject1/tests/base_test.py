import pytest
from utils.screenshot_utils import take_step_screenshot
from utils.logger import setup_logger
from pages_playwright.login_page_playwright import LoginPage
from pages_playwright.products_page_playwright import ProductsPage
from pages_playwright.cart_page_playwright import CartPage
from pages_playwright.checkout_info_page_playwright import CheckoutInfoPage
from pages_playwright.checkout_overview_page_playwright import CheckoutOverviewPage
from pages_playwright.checkout_complete_page_playwright import CheckoutCompletePage

LOGGER = setup_logger()

@pytest.mark.asyncio
class BaseTest:

    async def login_and_go_products(self, page):
        await page.goto("https://www.saucedemo.com/")
        LOGGER.info("Navigated to homepage")
        await take_step_screenshot(page, "01_home")
        login = LoginPage(page)
        await login.login("standard_user", "secret_sauce")
        LOGGER.info("Logged in")
        await take_step_screenshot(page, "02_logged_in")
        return ProductsPage(page)

    async def add_and_cart(self, page):
        products = await self.login_and_go_products(page)
        assert await products.is_title_visible()
        await take_step_screenshot(page, "03_products")
        await products.add_backpack_to_cart()
        await take_step_screenshot(page, "04_added_to_cart")
        await products.go_to_cart()
        LOGGER.info("Went to cart")
        return CartPage(page)

    async def checkout_flow(self, page):
        cart = await self.add_and_cart(page)
        assert await cart.verify_item("Sauce Labs Backpack")
        await take_step_screenshot(page, "05_cart_verified")
        await cart.click_checkout()
        LOGGER.info("Clicked checkout")
        await take_step_screenshot(page, "06_checkout_info")
        info = CheckoutInfoPage(page)
        await info.enter_info("John", "Doe", "12345")
        await take_step_screenshot(page, "07_info_entered")
        overview = CheckoutOverviewPage(page)
        assert await overview.verify_title()
        await take_step_screenshot(page, "08_overview")
        await overview.click_finish()
        await take_step_screenshot(page, "09_finished")
        complete = CheckoutCompletePage(page)
        assert await complete.verify_complete()
        await take_step_screenshot(page, "10_complete")
        LOGGER.info("Checkout complete")
        return complete
