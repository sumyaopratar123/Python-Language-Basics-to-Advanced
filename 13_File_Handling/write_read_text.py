# Python Basics to Advanced Example
# Run: python write_read_text.py

from pathlib import Path

path = Path("example.txt")
path.write_text("Hello from Python!\n", encoding="utf-8")
print(path.read_text(encoding="utf-8"))
