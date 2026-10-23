# Python Basics to Advanced Example
# Run: python context_manager.py

from contextlib import contextmanager

@contextmanager
def managed_message():
    print("Enter")
    try: yield "resource"
    finally: print("Exit")

with managed_message() as value: print(value)
