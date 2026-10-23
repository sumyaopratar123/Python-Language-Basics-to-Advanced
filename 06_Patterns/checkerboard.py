# Python Basics to Advanced Example
# Run: python checkerboard.py

n = int(input("Size: "))
for r in range(n): print(" ".join("■" if (r+c)%2==0 else "□" for c in range(n)))
