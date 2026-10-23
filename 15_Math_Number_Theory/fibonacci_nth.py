# Python Basics to Advanced Example
# Run: python fibonacci_nth.py

def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a+b
    return a

print(fib(10))
