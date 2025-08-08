class CartPage:
    def __init__(self, page):
        self.page = page

    def verify_item(self, item_name: str) -> bool:
        locator = self.page.locator(".inventory_item_name")
        return locator.inner_text() == item_name

    def click_checkout(self):
        self.page.click('[data-test="checkout"]')
