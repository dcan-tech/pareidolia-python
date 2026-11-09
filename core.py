"""Core image-generation logic for Pareidolia.

Split out from the original single-file pareidolia.py so this module
can be imported on its own (by a future GUI, test suite, etc.) without
pulling in argparse / CLI argument parsing. See cli.py for the
command-line entry point.
"""

import os
import numpy as np
from PIL import Image


def generate_image(width, height, seed=None, mode="grayscale"):
    """Generate one frame of random static as a PIL Image.

    Uses NumPy to build the whole pixel array in one call instead of
    writing pixels one at a time with Image.putpixel() — roughly
    100-200x faster for larger images.
    """
    rng = np.random.default_rng(seed)
    # NOTE: np.random.Generator (PCG64) is a different algorithm from
    # Python's random.Random, so a given seed produces different pixel
    # values than the original putpixel-based version did. Reproducible
    # within this version, same seed -> same output, every time.

    if mode == "grayscale":
        # Single-channel (L) array instead of a 3-channel RGB image
        # with equal R/G/B values — 1/3 the memory for grayscale.
        pixels = rng.integers(0, 256, size=(height, width), dtype=np.uint8)
        image = Image.fromarray(pixels, mode="L")
    elif mode == "rgb":
        pixels = rng.integers(0, 256, size=(height, width, 3), dtype=np.uint8)
        image = Image.fromarray(pixels, mode="RGB")
    else:
        # generate_image() validates its own input rather than relying
        # on the caller (e.g. argparse's choices=[...]) to have done so,
        # since this function can now be imported and called directly.
        raise ValueError(f"Unknown mode: {mode!r} (expected 'grayscale' or 'rgb')")

    return image


def generate_frames(width, height, seed=None, mode="grayscale", frame_count=1):
    """Generate frame_count frames, saving each as output/frame-NNN.png."""
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
    """Combine saved frame-*.png files into an animated GIF.

    loop=0 means loop forever (imageio's own default); pass loop=1 for
    "play once", or any N to loop N times.
    """
    from glob import glob
    import imageio.v2 as imageio
    # Imports kept local to this function so imageio is only required
    # when GIF creation is actually used.

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
