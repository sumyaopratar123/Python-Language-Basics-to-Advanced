# Python Basics to Advanced Example
# Run: python safe_file_copy.py

from pathlib import Path
import shutil

source = Path("source.txt")
target = Path("source_copy.txt")
if source.exists():
    shutil.copy2(source, target)
    print("Copied to", target)
else:
    print("Create source.txt first.")
