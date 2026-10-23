# Python Basics to Advanced Example
# Run: python recursive_fibonacci.py

from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(30))
