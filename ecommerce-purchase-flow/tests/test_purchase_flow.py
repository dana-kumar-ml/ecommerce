# tests/test_checkout_flow.py

import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutYourInformationPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage
from utils.screenshot_helper import take_screenshot
from utils.gif_creator import create_gif

import logging
logger = logging.getLogger(__name__)

# ---------- Test Steps (Grouped as Functions) ----------

def launch_site_and_login(driver):
    logger.info("Navigating to SauceDemo login page")
    driver.get("https://www.saucedemo.com/")
    take_screenshot(driver, "01_login_page")

    logger.info("Logging in as standard_user")
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    take_screenshot(driver, "02_after_login")

def verify_and_add_product_to_cart(driver):
    logger.info("Verifying product page title")
    products_page = ProductsPage(driver)
    assert products_page.verify_products_title()
    take_screenshot(driver, "03_products_title")

    logger.info("Adding backpack to cart")
    products_page.add_backpack_to_cart()
    take_screenshot(driver, "04_backpack_added")

def go_to_cart_and_validate(driver):
    logger.info("Navigating to cart")
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    take_screenshot(driver, "05_cart_page")

    logger.info("Verifying cart contains backpack")
    cart_page = CartPage(driver)
    assert cart_page.verify_item("Sauce Labs Backpack")
    take_screenshot(driver, "06_cart_verified")

    logger.info("Proceeding to checkout")
    cart_page.proceed_to_checkout()
    take_screenshot(driver, "07_checkout_info")

def fill_checkout_info(driver):
    logger.info("Entering checkout info")
    info_page = CheckoutYourInformationPage(driver)
    info_page.enter_info("John", "Doe", "12345")
    take_screenshot(driver, "08_info_entered")

def complete_checkout(driver):
    logger.info("Verifying checkout overview")
    overview_page = CheckoutOverviewPage(driver)
    assert overview_page.is_overview_displayed()
    take_screenshot(driver, "09_checkout_overview")

    logger.info("Finishing checkout")
    overview_page.finish()
    take_screenshot(driver, "10_checkout_complete")

    logger.info("Verifying success page")
    complete_page = CheckoutCompletePage(driver)
    assert complete_page.verify_success()
    take_screenshot(driver, "11_order_success")

# ---------- Main Test Case ----------

@pytest.mark.order(1)
def test_saucedemo_purchase_flow(driver):
    launch_site_and_login(driver)
    verify_and_add_product_to_cart(driver)
    go_to_cart_and_validate(driver)
    fill_checkout_info(driver)
    complete_checkout(driver)


    logger.info("Test completed successfully — creating GIF")
    create_gif(folder="tests/screenshots", output="tests/test_flow.gif")
