
"""Command-line interface for Pareidolia."""

import os
import argparse

from core import generate_image, generate_frames, create_gif_from_frames


def main():
    """Parse arguments and generate images or animations."""
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
        "--frames", type=int, default=1, help="Number of frames to generate (default: 1)"
    )
    parser.add_argument(
        "--animate",
        action="store_true",
        help="If set, combines frames into an animated GIF",
    )
    parser.add_argument(
        "--loop", type=int, default=0,
        help="GIF loop count: 0 = infinite (default), 1 = play once, N = loop N times",
    )
    args = parser.parse_args()

    os.makedirs("output", exist_ok=True)

    if args.frames > 1:
        generate_frames(args.width, args.height, args.seed, args.mode, args.frames)
        if args.animate:
            create_gif_from_frames(loop=args.loop)
    else:
        image = generate_image(args.width, args.height, args.seed, args.mode)

        filename = f"image-{args.width}x{args.height}"
        if args.seed is not None:
            filename += f"-seed{args.seed}"
        filename += ".png"

        filepath = os.path.join("output", filename)
        image.save(filepath)
        print(f"Image saved as: {filepath}")


if __name__ == "__main__":
    main()
