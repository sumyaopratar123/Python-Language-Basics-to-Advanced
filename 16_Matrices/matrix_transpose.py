# Python Basics to Advanced Example
# Run: python matrix_transpose.py

matrix = [[1, 2, 3], [4, 5, 6]]
print([list(row) for row in zip(*matrix)])
