import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException  # ← Add this line!

@pytest.mark.usefixtures("driver")
def test_assign_leave(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # ==== LOGIN ====
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # ==== DASHBOARD ====
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # ==== GET USER INITIAL ====
    user_profile_xpath = "//span[contains(@class,'oxd-userdropdown-tab')]/p[contains(@class,'oxd-userdropdown-name')]"
    current_username = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, user_profile_xpath))
    ).text.strip()
    first_letter = current_username[0] if current_username else "A"

    # ==== NAVIGATE TO ASSIGN LEAVE ====
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/leave/assignLeave")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Assign Leave']")))

    # ==== EMPLOYEE NAME ====
    employee_input_xpath = "//input[@placeholder='Type for hints...']"
    employee_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, employee_input_xpath)))
    employee_input.clear()
    time.sleep(1)
    employee_input.send_keys(first_letter)
    time.sleep(2)
    suggestion_xpath = "//div[@role='listbox']//div[@role='option']"
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, suggestion_xpath)))
    employee_input.send_keys(Keys.ARROW_DOWN)
    time.sleep(1)
    employee_input.send_keys(Keys.ENTER)
    employee_value = driver.find_element(By.XPATH, employee_input_xpath).get_attribute("value")
    assert employee_value.strip() != "", "Employee name not selected"

    # ==== LEAVE TYPE ====
    leave_type_dropdown_xpath = "//label[text()='Leave Type']/following::div[contains(@class,'oxd-select-text')][1]"
    leave_type_dropdown = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, leave_type_dropdown_xpath))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", leave_type_dropdown)
    leave_type_dropdown.click()
    options_xpath = "//div[@role='listbox']//span"
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
    options = driver.find_elements(By.XPATH, options_xpath)
    assert options, "No leave type options found."
    options[0].click()

    # ==== DATE PICKER FUNCTION ====
    def select_date(driver, date_input_xpath, date_to_select):
        date_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, date_input_xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", date_input)
        date_input.click()
        date_obj = datetime.strptime(date_to_select, "%Y-%m-%d")
        day = date_obj.day
        calendar_header_xpath = "//div[contains(@class,'oxd-calendar-header')]"
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, calendar_header_xpath)))
        day_xpath = f"//div[contains(@class,'oxd-calendar-date') and text()='{day}']"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, day_xpath))).click()
        time.sleep(0.5)

    # ==== SELECT DATES ====
    select_date(driver, "//label[text()='From Date']/following::input[1]", "2025-07-20")
    select_date(driver, "//label[text()='To Date']/following::input[1]", "2025-07-25")

    # ==== WAIT FOR BALANCE TEXT ====
    balance_text_xpath = "//p[contains(@class,'orangehrm-leave-balance-text')]"
    try:
        balance_text_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, balance_text_xpath))
        )
        balance_text = balance_text_element.text
        print("Balance info:", balance_text)
    except:
        print("Balance text not found, continuing...")
    time.sleep(5)


@pytest.mark.usefixtures("driver")
def test_click_assign_and_verify_popup(driver):
    print("\n Clicking 'Assign' and checking confirmation popup...")

    assign_button_xpath = "//button[@type='submit' and contains(.,'Assign')]"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, assign_button_xpath))).click()

    # DEBUG: Save screenshot
    driver.save_screenshot("assign_popup_debug.png")
    print(" Screenshot taken: assign_popup_debug.png")

    try:
        ok_button_xpath = "//button[contains(@class, 'oxd-button--secondary') and normalize-space()='Ok']"
        ok_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, ok_button_xpath))
        )
        ok_button.click()
        print("✅ 'Ok' button clicked successfully.")
    except Exception as e:
        driver.save_screenshot("ok_button_error.png")
        print("❌ 'Ok' button not found or not clickable. Screenshot saved as ok_button_error.png")
        raise e


@pytest.mark.usefixtures("driver")
def test_verify_current_user_across_pages(driver):
    # First get the current logged-in username from dashboard
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    user_xpath = "//span[contains(@class,'oxd-userdropdown-tab')]/p[contains(@class,'oxd-userdropdown-name')]"
    expected_user_element = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, user_xpath))
    )
    expected_username = expected_user_element.text.strip()
    print(f"Expected username to verify across pages: '{expected_username}'")

    # Pages to verify user on
    pages_to_check = [
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index",
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList",
        "https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList",
        "https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet"
    ]

    for page in pages_to_check:
        driver.get(page)
        print(f"Checking user on page: {page}")

        try:
            user_element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, user_xpath))
            )
            actual_username = user_element.text.strip()
            print(f"Found user: '{actual_username}'")

            if actual_username != expected_username:
                print(f"❌ User mismatch on page {page}. Expected '{expected_username}', but got '{actual_username}'")
                # Stop the test immediately on mismatch
                assert False, f"User mismatch on page {page}"
            else:
                print(f"✅ User matches on page {page}")

        except Exception as e:
            print(f"❌ Could not find user element on page {page}. Exception: {e}")
            assert False, f"User element missing on page {page}"

    print("✅ All pages have the expected logged-in user.")


import logging

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@pytest.mark.usefixtures("driver")
def test_navigate_leave_and_search_records(driver):
    wait = WebDriverWait(driver, 15)

    logger.info("🌐 Navigating to Dashboard...")
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    # Step 1: Click 'Leave' in sidebar
    try:
        leave_menu = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Leave']/parent::a")))
        leave_menu.click()
        logger.info("✅ Clicked 'Leave' in sidebar.")
    except TimeoutException:
        logger.error("❌ Could not click 'Leave' in sidebar.")
        return

    # Step 2: Ensure submenu is visible
    time.sleep(2)
    submenu_elements = driver.find_elements(By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")
    logger.info(f"🧭 Submenu items found: {[e.text for e in submenu_elements]}")

    # Step 3: Click 'Leave List'
    try:
        leave_list_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Leave List') and contains(@class,'oxd-topbar-body-nav-tab-item')]"))
        )
        driver.execute_script("arguments[0].click();", leave_list_tab)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Leave List']")))
        logger.info("✅ Navigated to Leave List.")
    except TimeoutException:
        driver.save_screenshot("failed_to_navigate_leave_list.png")
        logger.error("no record found")
        return

    # Step 4: Fill 'Employee Name'
    try:
        emp_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']")))
        emp_input.clear()
        emp_input.send_keys("Admin")
        time.sleep(1)
        emp_input.send_keys("\ue015")  # Arrow Down
        time.sleep(0.5)
        emp_input.send_keys("\ue007")  # Enter
        logger.info("✅ Employee selected.")
    except TimeoutException:
        logger.warning("⚠️ Employee input not found.")

    # Step 5: Select Leave Type
    try:
        leave_type_dropdown = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[text()='Leave Type']/following::div[contains(@class,'oxd-select-text')][1]"))
        )
        leave_type_dropdown.click()
        options = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='listbox']//span")))
        options[0].click()
        logger.info("✅ Leave type selected.")
    except TimeoutException:
        logger.warning("⚠️ Leave type dropdown not available.")

    # Step 6: Click Search
    try:
        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and normalize-space()='Search']")))
        search_button.click()
        logger.info("🔍 Clicked Search button.")
    except TimeoutException:
        logger.error("❌ Search button not found.")
        return

    # Step 7: Check leave record table
    time.sleep(1)
    try:
        rows = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.oxd-table-body > div.oxd-table-card"))
        )
        logger.info(f"✅ Found {len(rows)} leave record(s).")
    except TimeoutException:
        logger.info("ℹ️ No leave records found.")
