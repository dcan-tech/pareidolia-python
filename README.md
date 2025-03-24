# Pareidolia (Python Edition)

_A visual noise generator inspired by the original [Pareidolia Dart project](https://github.com/tytydraco/pareidolia) — rewritten in Python for experimentation, exploration, and education._

---

## Overview

This command-line application generates grayscale or RGB static noise images using random pixel data. It supports reproducible output via seeding, multi-frame generation, and optional animation via `.gif` creation.

Built as a fun coding exercise to reinforce CLI tooling, image manipulation, and randomization techniques in Python — with room to grow into more advanced pareidolia-style pattern exploration.

---

## Available Flags

| Flag         | Type    | Description                                                                 |
|--------------|---------|-----------------------------------------------------------------------------|
| `--width`    | `int`   | Width of the image (default: `128`)                                        |
| `--height`   | `int`   | Height of the image (default: `128`)                                       |
| `--mode`     | `str`   | Color mode: `grayscale` or `rgb` (default: `grayscale`)                     |
| `--seed`     | `int`   | Optional seed for reproducible randomness (default: `None`)                |
| `--frames`   | `int`   | Number of frames to generate (default: `1`)                                 |
| `--animate`  | *flag*  | If set, combines all generated frames into `animation.gif` (only if >1)     |

---

## Usage Example

```bash
python pareidolia.py --width 128 --height 128 --mode rgb --seed 42 --frames 1 --animate
```



## Output

- Single images saved as:
    - `output/image-WxH[-seedX].png`
- Frame batches saved as:
    - `output/frame-000.png`, `frame-001.png`, etc.
- Animated output (if `--animate` is used):
    - `output/animation.gif`

---

## Future Plans

- Additional color modes (palette cycling, sepia, heatmaps)
- Interactive GUI toggle (Tkinter or Web-based)
- Hidden pattern embedding for human/AI testing
- Export metadata to `.json` or `.csv`
- Modular code structure (split into `cli.py`, `core.py`, etc.)
- Optional filename builder with timestamp or user label

---

## Author
**Dylan Canfield**


