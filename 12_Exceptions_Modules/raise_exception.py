# Python Basics to Advanced Example
# Run: python raise_exception.py

def positive_square(n):
    if n < 0: raise ValueError("n must be non-negative")
    return n*n

print(positive_square(5))
