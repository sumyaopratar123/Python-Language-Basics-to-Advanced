# Python Basics to Advanced Example
# Run: python timedelta_demo.py

from datetime import date, timedelta

today = date.today()
print("Today:", today)
print("In 30 days:", today + timedelta(days=30))
