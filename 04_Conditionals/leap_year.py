# Python Basics to Advanced Example
# Run: python leap_year.py

year = int(input("Year: "))
print("Leap year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not leap year")
