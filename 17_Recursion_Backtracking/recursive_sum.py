# Python Basics to Advanced Example
# Run: python recursive_sum.py

def recursive_sum(n):
    return 0 if n <= 0 else n + recursive_sum(n-1)

print(recursive_sum(10))
