# Python Basics to Advanced Example
# Run: python append_file.py

from pathlib import Path

path = Path("log.txt")
with path.open("a", encoding="utf-8") as file:
    file.write("New log entry\n")
print("Entry appended.")
