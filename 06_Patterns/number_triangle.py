# Python Basics to Advanced Example
# Run: python number_triangle.py

n = int(input("Rows: "))
for i in range(1, n+1): print(" ".join(str(j) for j in range(1, i+1)))
