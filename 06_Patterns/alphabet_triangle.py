# Python Basics to Advanced Example
# Run: python alphabet_triangle.py

n = int(input("Rows (1-26): "))
for i in range(1, min(n, 26)+1): print(" ".join(chr(64+j) for j in range(1, i+1)))
