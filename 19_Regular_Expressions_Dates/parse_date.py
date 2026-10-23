# Python Basics to Advanced Example
# Run: python parse_date.py

from datetime import datetime

value = "23-10-2026"
parsed = datetime.strptime(value, "%d-%m-%Y")
print(parsed.date())
