import os
import imageio.v2 as imageio  # Use imageio.v2 to avoid the warning

def generate_gif(screenshots_dir="screenshots", output_path="tests_run.gif", duration=0.5):
    if not os.path.exists(screenshots_dir):
        print(f"No screenshots directory found at '{screenshots_dir}'")
        return

    files = sorted(
        [os.path.join(screenshots_dir, f) for f in os.listdir(screenshots_dir) if f.endswith(".png")]
    )

    if not files:
        print("No screenshots found to generate GIF.")
        return

    images = []
    for file_path in files:
        img = imageio.imread(file_path)
        images.append(img)

    imageio.mimsave(output_path, images, duration=duration)
    print(f"GIF generated at {output_path}")
