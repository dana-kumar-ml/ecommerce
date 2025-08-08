class CheckoutInfoPage:
    def __init__(self, page):
        self.page = page

    def enter_info(self, first_name: str, last_name: str, zip_code: str):
        self.page.fill('[data-test="firstName"]', first_name)
        self.page.fill('[data-test="lastName"]', last_name)
        self.page.fill('[data-test="postalCode"]', zip_code)
        self.page.click('[data-test="continue"]')
