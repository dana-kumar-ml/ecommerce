class CheckoutOverviewPage:
    def __init__(self, page):
        self.page = page

    def verify_title(self) -> bool:
        return self.page.locator(".title").inner_text() == "Checkout: Overview"

    def click_finish(self):
        self.page.click('[data-test="finish"]')
