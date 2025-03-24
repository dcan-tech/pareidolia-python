# Pareidolia Python

_A minimalist random image generator written in Python, inspired by the Dart-based [Pareidolia](https://github.com/tytydraco/pareidolia) project._

This project is being developed as a clean rewrite to explore core Python skills, creative image output, and optional neural-inspired enhancements.

---

## Features

- Generates random grayscale or RGB static
- Seeded randomness for repeatable image output
- Adjustable image size and color ranges
- Clean code structure with user-defined options planned

## Planned Enhancements

- **CLI support** with flags for mode, size, seed, etc.
- **Animated static** generation as GIFs or frame series
- Optional logic for **visualizing neural-inspired behavior**
- Export options: `.png`, `.gif`, maybe even `.csv` or `.json`
- Interactive patterns or deterministic grid generation
- Clean separation between logic, I/O, and CLI handling

## Tech Stack

- Python 3.10+
- [Pillow](https://python-pillow.org/) for image generation
- (Optional) `imageio` for animation
- (Optional) `argparse` for CLI inputs

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install pillow
```

## Usage

The base version will support the following:

```bash
python pareidolia.py --width 128 --height 128 --mode rgb --seed 42
```

Output will be saved to the `output/` directory by default.

---

## Author
**Dylan Canfield**

