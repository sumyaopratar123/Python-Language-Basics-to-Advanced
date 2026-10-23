# Python Basics to Advanced Example
# Run: python directory_listing.py

from pathlib import Path

for item in Path(".").iterdir():
    print("DIR " if item.is_dir() else "FILE", item.name)
