
"""Core image-generation functionality for Pareidolia."""

import os
import numpy as np
from PIL import Image


def generate_image(width, height, seed=None, mode="grayscale"):
    """Generate a frame of random static as a PIL Image."""
    rng = np.random.default_rng(seed)

    # NumPy uses a different random generator than the original
    # implementation. Identical seeds will produce different images.
    if mode == "grayscale":
        pixels = rng.integers(0, 256, size=(height, width), dtype=np.uint8)
        image = Image.fromarray(pixels, mode="L")
    elif mode == "rgb":
        pixels = rng.integers(0, 256, size=(height, width, 3), dtype=np.uint8)
        image = Image.fromarray(pixels, mode="RGB")
    else:
        raise ValueError(f"Unknown mode: {mode!r} (expected 'grayscale' or 'rgb')")

    return image


def generate_frames(width, height, seed=None, mode="grayscale", frame_count=1):
    """Generate and save numbered PNG frames in the output directory."""
    os.makedirs("output", exist_ok=True)

    for i in range(frame_count):
        image = generate_image(width, height, seed, mode)
        filename = f"frame-{i:03d}.png"
        filepath = os.path.join("output", filename)
        image.save(filepath)
        print(f"Saved: {filepath}")

        if seed is not None:
            seed += 1


def create_gif_from_frames(
        output_dir="output", pattern="frame-*.png", gif_name="animation.gif",
        duration=0.1, loop=0
):
    """Combine saved PNG frames into an animated GIF."""
    from glob import glob
    import imageio.v2 as imageio

    frames = []
    paths = sorted(glob(os.path.join(output_dir, pattern)))

    if not paths:
        print("No frame images found to build GIF.")
        return

    for path in paths:
        frames.append(imageio.imread(path))

    gif_path = os.path.join(output_dir, gif_name)
    imageio.mimsave(gif_path, frames, duration=duration, loop=loop)
    print(f"Animated GIF saved as: {gif_path}")
