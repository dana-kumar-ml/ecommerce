# utils/screenshot_helper.py

import os
from datetime import datetime

def take_screenshot(driver, name, folder="tests/screenshots"):
    os.makedirs(folder, exist_ok=True)  # ✅ Create the folder if missing
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{name}.png"
    path = os.path.join(folder, filename)
    driver.save_screenshot(path)
    return path
