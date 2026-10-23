# Python Basics to Advanced Example
# Run: python file_metadata.py

from pathlib import Path

path = Path(__file__)
print("Name:", path.name)
print("Suffix:", path.suffix)
print("Bytes:", path.stat().st_size)
