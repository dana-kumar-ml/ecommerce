class CheckoutCompletePage:
    def __init__(self, page):
        self.page = page

    def verify_complete(self) -> bool:
        return self.page.locator(".complete-header").inner_text() == "Thank you for your order!"
