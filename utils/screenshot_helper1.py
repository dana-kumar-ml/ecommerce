import os
from datetime import datetime

def take_screenshot(page, name, folder="tests/screenshots"):
    os.makedirs(folder, exist_ok=True)  # Create folder if it doesn't exist
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{name}.png"
    path = os.path.join(folder, filename)
    page.screenshot(path=path)  # ✅ Playwright-compatible
