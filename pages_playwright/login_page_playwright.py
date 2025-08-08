class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, username: str, password: str):
        self.page.fill('[data-test="username"]', username)
        self.page.fill('[data-test="password"]', password)
        self.page.click('[data-test="login-button"]')
