import pytest_asyncio

@pytest_asyncio.fixture(scope="session")
async def browser_manager():
    from playwright.async_api import async_playwright

    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=False)
    yield browser
    try:
        await browser.close()
    except Exception as e:
        print(f"Ignored exception on browser close: {e}")
    await playwright.stop()


@pytest_asyncio.fixture(scope="function")
async def page(browser_manager):
    # Create a new browser context and page for each test
    context = await browser_manager.new_context()
    page = await context.new_page()
    yield page
    await context.close()
