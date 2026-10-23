# Python Basics to Advanced Example
# Run: python any_all.py

values = [2, 4, 6]
print(all(v % 2 == 0 for v in values))
print(any(v > 5 for v in values))
