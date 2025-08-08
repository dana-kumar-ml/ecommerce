# utils/screenshot_utils.py
import os
from PIL import Image

SCREENSHOT_DIR = "screenshots"

def ensure_dir():
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

async def take_step_screenshot(page, step_name):
    ensure_dir()
    path = os.path.join(SCREENSHOT_DIR, f"{step_name}.png")
    await page.screenshot(path=path)
    return path

def generate_gif(output_path="screenshots/flow.gif", duration=700):
    ensure_dir()
    images = []
    for fname in sorted(os.listdir(SCREENSHOT_DIR)):
        if fname.endswith(".png"):
            images.append(Image.open(os.path.join(SCREENSHOT_DIR, fname)))
    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:], duration=duration, loop=0)
