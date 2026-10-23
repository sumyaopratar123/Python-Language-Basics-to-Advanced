# Python Basics to Advanced Example
# Run: python csv_summary.py

import csv
from pathlib import Path

path = Path("marks.csv")
if path.exists():
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print("Rows:", len(rows))
else:
    print("Create marks.csv with a header row first.")
