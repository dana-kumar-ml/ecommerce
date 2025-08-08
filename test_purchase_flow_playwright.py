import pytest
from playwright.sync_api import Page

# ✅ Playwright-based Page Object imports
from pages_playwright.login_page_playwright import LoginPage
from pages_playwright.products_page_playwright import ProductsPage
from pages_playwright.cart_page_playwright import CartPage
from pages_playwright.checkout_info_page_playwright import CheckoutInfoPage
from pages_playwright.checkout_overview_page_playwright import CheckoutOverviewPage
from pages_playwright.checkout_complete_page_playwright import CheckoutCompletePage

# ✅ Screenshot and GIF utilities
from utils.screenshot_helper1 import take_screenshot
from utils.gif_creator import create_gif

import logging
logger = logging.getLogger(__name__)

# ---------- Test Steps (Encapsulated Functions) ----------

def launch_site_and_login(page: Page):
    logger.info("Navigating to SauceDemo login page")
    page.goto("https://www.saucedemo.com/")
    take_screenshot(page, "01_login_page")

    logger.info("Logging in as standard_user")
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    take_screenshot(page, "02_after_login")

def verify_and_add_product_to_cart(page: Page):
    logger.info("Verifying product page title")
    products_page = ProductsPage(page)
    assert products_page.is_title_visible(), "Product title verification failed"
    take_screenshot(page, "03_products_title")

    logger.info("Adding backpack to cart")
    products_page.add_backpack_to_cart()
    take_screenshot(page, "04_backpack_added")

def go_to_cart_and_validate(page: Page):
    logger.info("Navigating to cart")
    page.click(".shopping_cart_link")
    take_screenshot(page, "05_cart_page")

    logger.info("Verifying cart contains backpack")
    cart_page = CartPage(page)
    assert cart_page.verify_item("Sauce Labs Backpack"), "Backpack not found in cart"
    take_screenshot(page, "06_cart_verified")

    logger.info("Proceeding to checkout")
    cart_page.click_checkout()
    take_screenshot(page, "07_checkout_info")

def fill_checkout_info(page: Page):
    logger.info("Entering checkout info")
    info_page = CheckoutInfoPage(page)
    info_page.enter_info("John", "Doe", "12345")
    take_screenshot(page, "08_info_entered")

def complete_checkout(page: Page):
    logger.info("Verifying checkout overview")
    overview_page = CheckoutOverviewPage(page)
    assert overview_page.verify_title(), "Checkout overview not displayed"
    take_screenshot(page, "09_checkout_overview")

    logger.info("Finishing checkout")
    overview_page.click_finish()
    take_screenshot(page, "10_checkout_complete")

    logger.info("Verifying success page")
    complete_page = CheckoutCompletePage(page)
    assert complete_page.verify_complete(), "Order success not verified"
    take_screenshot(page, "11_order_success")

# ---------- Main Test Case ----------

@pytest.mark.order(1)
def test_saucedemo_purchase_flow(page: Page):
    """End-to-end checkout flow on SauceDemo using Playwright + Pytest"""
    launch_site_and_login(page)
    verify_and_add_product_to_cart(page)
    go_to_cart_and_validate(page)
    fill_checkout_info(page)
    complete_checkout(page)

    logger.info("Test completed successfully — creating GIF")
    create_gif(folder="tests/screenshots", output="tests/test_flow.gif")
