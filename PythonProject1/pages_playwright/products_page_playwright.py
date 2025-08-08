from .base_page_playwright import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page_title = "span.title"
        self.add_backpack_button = "button[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_button = "a.shopping_cart_link"  # selector for the cart icon/button

    async def is_title_visible(self) -> bool:
        await self.page.wait_for_selector(self.page_title, state="visible")
        await self.highlight(self.page_title)
        return await self.page.is_visible(self.page_title)

    async def add_backpack_to_cart(self):
        await self.wait_and_click(self.add_backpack_button)

    async def go_to_cart(self):
        # Click on the cart button to navigate to the cart page
        await self.wait_and_click(self.cart_button)
