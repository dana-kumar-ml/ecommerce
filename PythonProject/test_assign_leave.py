import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

@pytest.fixture
def driver():
    service = Service(executable_path="path/to/chromedriver")  # 🔁 Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_assign_leave(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Navigate to Assign Leave
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Leave"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Assign Leave"))).click()

    # Fill out Assign Leave form
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type for hints...']"))).send_keys("Orange Test")
    time.sleep(1)  # Allow auto-suggest dropdown to appear
    driver.find_element(By.XPATH, "//div[@role='option']").click()

    driver.find_element(By.XPATH, "//label[text()='Leave Type']/following::div[1]").click()
    driver.find_element(By.XPATH, "//span[text()='Annual Leave']").click()

    # Set From and To Date
    driver.find_element(By.XPATH, "//label[text()='From Date']/following::input[1]").send_keys("2025-07-20")
    driver.find_element(By.XPATH, "//label[text()='To Date']/following::input[1]").send_keys("2025-07-20")

    driver.find_element(By.XPATH, "//textarea").send_keys("Test leave assignment.")

    # Click Assign
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Handle popup (confirmation alert)
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        print("Popup appeared: ", alert.text)
        alert.accept()  # Click OK
    except NoAlertPresentException:
        print("No alert popup appeared.")

    # Optional: Add assertion or verification here
    time.sleep(3)
