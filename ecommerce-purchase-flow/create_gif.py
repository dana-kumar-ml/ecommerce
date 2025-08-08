# utils/gif_creator.py
import os
import imageio

def create_gif(screenshot_dir="tests/screenshots", output_path="gifs/final_output.gif"):
    os.makedirs("gifs", exist_ok=True)
    images = []
    for file in sorted(os.listdir(screenshot_dir)):
        if file.endswith(".png"):
            path = os.path.join(screenshot_dir, file)
            images.append(imageio.imread(path))
    if images:
        imageio.mimsave(output_path, images, duration=1)
