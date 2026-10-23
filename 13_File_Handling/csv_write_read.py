# Python Basics to Advanced Example
# Run: python csv_write_read.py

import csv
from pathlib import Path

path = Path("people.csv")
with path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Asha", 20])
with path.open(newline="", encoding="utf-8") as f:
    print(list(csv.DictReader(f)))
