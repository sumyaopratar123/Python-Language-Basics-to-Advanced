# Python Basics to Advanced Example
# Run: python decorator.py

from functools import wraps

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@announce
def add(a, b): return a+b

print(add(2, 3))
