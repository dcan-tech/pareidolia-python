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


def generate_frames(width, height, seed=None, mode="grayscale", frame_count=1):
    os.makedirs("output", exist_ok=True)

    for i in range(frame_count):
        image = generate_image(width, height, seed, mode)
        filename = f"frame-{i:03d}.png"
        filepath = os.path.join("output", filename)
        image.save(filepath)
        print(f"Saved: {filepath}")

        if seed is not None:
            seed += 1


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
parser.add_argument(
    "--frames",
    type=int,
    default=1,
    help="Number of frames to generate (default: 1)"
)

args = parser.parse_args()

# use arguments
width = args.width
height = args.height
seed = args.seed
rng = random.Random(seed)
mode = args.mode
frame_count = args.frames

if frame_count > 1:
    generate_frames(width, height, seed, mode, frame_count)
else:
    image = generate_image(width, height, seed, mode)

    filename = f"image-{width}x{height}"
    if seed is not None:
        filename += f"-seed{seed}"
    filename += ".png"

    filepath = os.path.join("output", filename)
    image.save(filepath)
    print(f"Image saved as: {filepath}")



# output directory exists?
os.makedirs("output", exist_ok=True)




