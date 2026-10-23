# Python Basics to Advanced Example
# Run: python recursive_factorial.py

def factorial(n):
    if n < 0: raise ValueError("n must be non-negative")
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(5))
