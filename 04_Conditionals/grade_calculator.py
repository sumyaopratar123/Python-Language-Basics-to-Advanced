# Python Basics to Advanced Example
# Run: python grade_calculator.py

marks = float(input("Marks (0-100): "))
if not 0 <= marks <= 100: print("Invalid marks")
elif marks >= 90: print("A")
elif marks >= 80: print("B")
elif marks >= 70: print("C")
elif marks >= 60: print("D")
else: print("Needs improvement")
