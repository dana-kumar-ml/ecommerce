import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


@pytest.fixture
def driver():
    # Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    # Teardown
    driver.quit()


def test_random_article(driver):
    driver.get("https://www.wikipedia.org/")

    # Click English
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "js-link-box-en"))
    ).click()

    # Wait for main page content
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    time.sleep(1)  # Optional: Allow UI animations to complete

    # Open hamburger menu if needed (for mobile layout)
    try:
        checkbox = driver.find_element(By.ID, "vector-main-menu-dropdown-checkbox")
        if not checkbox.is_selected():
            driver.execute_script("arguments[0].click();", checkbox)
            time.sleep(1)
    except:
        pass  # No menu found — likely desktop layout

    # Click "Random article"
    random_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Random"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", random_link)
    random_link.click()

    # Wait for article heading
    heading_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )

    article_heading = heading_element.text
    print("Article Heading:", article_heading)

    # Validate it's not the main page
    assert driver.current_url != "https://en.wikipedia.org/wiki/Main_Page", "Did not navigate to a random article."
    assert driver.title != "Wikipedia, the free encyclopedia", "Title indicates main page."

    print("Random article loaded.")
    print("Title:", driver.title)
    print("URL:", driver.current_url)
