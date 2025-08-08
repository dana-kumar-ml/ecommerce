import os
from PIL import Image

def create_gif(folder="tests/screenshots", output="test_flow.gif", duration=800):
    images = []
    files = sorted(os.listdir(folder))
    for file in files:
        if file.endswith(".png"):
            img_path = os.path.join(folder, file)
            images.append(Image.open(img_path))

    if images:
        images[0].save(
            output,
            save_all=True,
            append_images=images[1:],
            duration=duration,
            loop=0
        )
        print(f"✅ GIF saved as: {output}")
    else:
        print("❌ No screenshots found to generate GIF.")
