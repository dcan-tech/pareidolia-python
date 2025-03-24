import os
import random
from PIL import Image
import argparse

# CLI argument parser
parser = argparse.ArgumentParser(description="Generate random static images.")
parser.add_argument("--width", type=int, default=128, help="Width of image")
parser.add_argument("--height", type=int, default=128, help="Height of image")
parser.add_argument("--seed", type=int, default=None, help="Optional random seed")

args = parser.parse_args()

# use arguments
width = args.width
height = args.height
seed = args.seed
rng = random.Random(seed)



# output directory exists?
os.makedirs("output", exist_ok=True)



# create a new RGB imagae
image = Image.new("RGB", (width, height))

for x in range(width):
    for y in range(height):
        gray = rng.randint(0, 255)
        image.putpixel((x, y), (gray, gray, gray))

image.save("output/image.png")
