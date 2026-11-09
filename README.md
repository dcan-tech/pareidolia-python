# Pareidolia (Python Edition)

A visual noise generator inspired by the original Pareidolia Dart library — rewritten in Python for experimentation, exploration, and education.

## Overview

This command-line application generates grayscale or RGB static noise images using random pixel data. It supports reproducible output via seeding, multi-frame generation, and optional animation via `.gif` creation.

Built as a fun coding exercise to reinforce CLI tooling, image manipulation, and randomization techniques in Python — with room to grow into more advanced pareidolia-style pattern exploration.

## Project Structure

| File | Purpose |
|---|---|
| `core.py` | Image/frame/GIF generation logic — importable standalone |
| `cli.py` | Command-line argument parsing, calls into `core.py` |
| `pareidolia.py` | Backward-compatible wrapper; `python pareidolia.py ...` still works exactly as before, now via `cli.py` |

## Available Flags

| Flag | Type | Description |
|---|---|---|
| `--width` | int | Width of the image (default: 128) |
| `--height` | int | Height of the image (default: 128) |
| `--mode` | str | Color mode: `grayscale` or `rgb` (default: `grayscale`) |
| `--seed` | int | Optional seed for reproducible randomness (default: `None`) |
| `--frames` | int | Number of frames to generate (default: 1) |
| `--animate` | flag | If set, combines all generated frames into `animation.gif` (only if `--frames` > 1) |
| `--loop` | int | GIF loop count: `0` = infinite (default), `1` = play once, `N` = loop N times |

## Usage Example

```bash
python pareidolia.py --width 128 --height 128 --mode rgb --seed 42 --frames 1 --animate
```

## Output

- Single images saved as: `output/image-WxH[-seedX].png`
- Frame batches saved as: `output/frame-000.png`, `output/frame-001.png`, etc.
- Animated output (if `--animate` is used): `output/animation.gif`

## Changelog

- **Performance:** image generation now uses NumPy array generation instead of a per-pixel loop — roughly 100–200x faster for larger images. Note: this changed the RNG algorithm (NumPy's PCG64 instead of Python's `random.Random`), so a given `--seed` now produces different pixel values than in earlier versions. Reproducibility *within* the current version is unaffected.
- **Added:** `--loop` flag for GIF loop count.
- **Refactored:** split into `core.py` (generation logic) and `cli.py` (argument parsing), with `pareidolia.py` kept as a backward-compatible entry point.

## Requirements

```bash
pip install pillow numpy imageio
```

## Future Plans

- Additional color modes (palette cycling, sepia, heatmaps)
- Interactive GUI toggle (Tkinter or Web-based)
- Hidden pattern embedding for human/AI testing
- Export metadata to `.json` or `.csv`
- Optional filename builder with timestamp or user label

## Author

Dylan Canfield
