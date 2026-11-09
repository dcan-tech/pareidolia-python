"""Backward-compatible entry point.

The project is now split into core.py (image/frame/gif generation)
and cli.py (argument parsing). This file exists only so that
`python pareidolia.py ...` keeps working exactly as before the split.
New code should import from core.py directly, or run cli.py.
"""

from cli import main

if __name__ == "__main__":
    main()
