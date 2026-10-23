# Python Basics to Advanced Example
# Run: python sum_first_n.py

n = int(input("n: "))
print(sum(range(1, n+1)) if n >= 0 else "Enter a non-negative integer")
