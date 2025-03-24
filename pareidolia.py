import os
import random
from PIL import Image


# output directory exists?
os.makedirs("output", exist_ok=True)

# image size
width, height = 128, 128

# create a new RGB imagae
image = Image.new("RGB", (width, height))

for x in range(width):
    for y in range(height):
        gray = random.randint(0, 255)
        image.putpixel((x, y), (gray, gray, gray))

image.save("output/image.png")
