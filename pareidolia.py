import os
import random
from PIL import Image
import argparse

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

# use arguments
width = args.width
height = args.height
seed = args.seed
rng = random.Random(seed)
mode = args.mode


# output directory exists?
os.makedirs("output", exist_ok=True)

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

# create a new RGB image
image = generate_image(width, height, seed, mode)



# build dynamic filename
filename = f"image-{width}x{height}"
if seed is not None:
    filename += f"-seed{seed}"
filename += ".png"

# save image
image.save(os.path.join("output", filename))
