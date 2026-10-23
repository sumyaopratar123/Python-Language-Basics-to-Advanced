# Python Basics to Advanced Example
# Run: python read_lines.py

from pathlib import Path

path = Path("sample.txt")
if path.exists():
    for line in path.read_text(encoding="utf-8").splitlines(): print(line)
else:
    print("Create sample.txt first.")
