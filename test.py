import os
import random
from PIL import Image
import argparse

def generate_image(width, height, seed=None, mode="grayscale"):
    rng = random.Random(seed)
    image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            if mode == "grayscale":
                gray = rng.randint(0, 255)
                color = (gray, gray, gray)
            else:
                r = rng.randint(0, 255)
                g = rng.randint(0, 255)
                b = rng.randint(0, 255)
                color = (r, g, b)

            image.putpixel((x, y), color)

    return image

# CLI argument parser
parser = argparse.ArgumentParser(description="Generate random static images.")
parser.add_argument("--width", type=int, default=128, help="Width of image")
parser.add_argument("--height", type=int, default=128, help="Height of image")
parser.add_argument("--seed", type=int, default=None, help="Optional random seed")
parser.add_argument(
    "--mode",
    type=str,
    choices=["grayscale", "rgb"],
    default="grayscale",
    help="Color mode: grayscale or rgb (default: grayscale)",
)
args = parser.parse_args()

width = args.width
height = args.height
seed = args.seed
mode = args.mode

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Interactive filename selection loop
while True:
    filename = input("Enter filename (or leave blank to use default): ").strip()
    if not filename:
        filename = f"image-{width}x{height}"
        if seed is not None:
            filename += f"-seed{seed}"
        filename += ".png"

    filepath = os.path.join("output", filename)
    if os.path.exists(filepath):
        print(f"File '{filename}' already exists. Please choose a new name.")
    else:
        break

# Generate and save the image
image = generate_image(width, height, seed, mode)
image.save(filepath)
print(f"Image saved as: {filepath}")
