from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    username_display = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    dashboard_menu = (By.XPATH, "//span[text()='Dashboard']")
    myinfo_menu = (By.XPATH, "//span[text()='My Info']")

    def get_username(self):
        return self.get_text(self.username_display)

    def go_to_dashboard(self):
        self.click(self.dashboard_menu)

    def go_to_my_info(self):
        self.click(self.myinfo_menu)
