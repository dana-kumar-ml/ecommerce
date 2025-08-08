from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def highlight(self, element):
        """Visually highlight the element by applying a red border."""
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)

    def find(self, by, locator):
        """Wait for presence of element and highlight it."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )
        self.highlight(element)
        return element

    def click(self, by, locator):
        """Wait for element to be clickable, highlight it, and click."""
        element = WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        self.highlight(element)
        element.click()

    def type(self, by, locator, text):
        """Clear the input field, highlight it, and type the given text."""
        element = self.find(by, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, locator):
        """Get text from a visible element."""
        return self.find(by, locator).text

    def is_visible(self, by, locator):
        """Check if an element is visible on the page."""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            self.highlight(element)
            return element.is_displayed()
        except:
            return False
