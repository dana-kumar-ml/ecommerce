class ProductsPage:
    def __init__(self, page):
        self.page = page

    def is_title_visible(self) -> bool:
        return self.page.locator(".title").inner_text() == "Products"

    def add_backpack_to_cart(self):
        self.page.click('[data-test="add-to-cart-sauce-labs-backpack"]')
