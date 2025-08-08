from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.type(By.ID, "txtUsername", username)
        self.type(By.ID, "txtPassword", password)
        self.click(By.ID, "btnLogin")

    def get_logged_in_username(self):
        return self.get_text(By.ID, "welcome")
