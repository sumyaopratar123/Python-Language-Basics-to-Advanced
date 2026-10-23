# Python Basics to Advanced Example
# Run: python matrix_addition.py

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
print([[a[i][j]+b[i][j] for j in range(2)] for i in range(2)])
