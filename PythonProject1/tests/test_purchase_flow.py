import pytest
from tests.base_test import BaseTest
from utils.screenshot_utils import generate_gif
from utils.logger import setup_logger

LOGGER = setup_logger()

@pytest.mark.asyncio
class TestPurchaseFlow(BaseTest):

    async def test_full_purchase(self, page):
        LOGGER.info("Starting full purchase test")
        await self.checkout_flow(page)
        LOGGER.info("Full purchase test completed")

    async def test_all_steps(self, page):
        LOGGER.info("Starting all steps test")
        await self.login_and_go_products(page)
        await self.add_and_cart(page)
        await self.checkout_flow(page)
        LOGGER.info("All steps test completed")

# Run this once per session after all tests complete
@pytest.fixture(scope="session", autouse=True)
def finalize():
    yield
    generate_gif()
