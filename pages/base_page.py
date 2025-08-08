import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, highlight=True, wait_time=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait_time)
        self.highlight_enabled = highlight

    def wait_and_find(self, by_locator):
        element = self.wait.until(EC.visibility_of_element_located(by_locator))
        if self.highlight_enabled:
            self._highlight(element)
        return element

    def click(self, by_locator):
        element = self.wait_and_find(by_locator)
        element.click()

    def type(self, by_locator, text):
        element = self.wait_and_find(by_locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, by_locator):
        return self.wait_and_find(by_locator).text

    def _highlight(self, element, duration=1, color="yellow", border="2px solid red"):
        original_style = element.get_attribute("style")
        highlight_style = f"background-color: {color}; border: {border};"
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element, highlight_style
        )
        time.sleep(duration)  # actual pause here
        self.driver.execute_script(
            "arguments[0].setAttribute('style', arguments[1]);",
            element, original_style
        )
