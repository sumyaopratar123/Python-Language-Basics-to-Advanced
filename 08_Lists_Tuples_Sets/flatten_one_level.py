# Python Basics to Advanced Example
# Run: python flatten_one_level.py

nested = [[1, 2], [3, 4], [5]]
print([item for group in nested for item in group])
