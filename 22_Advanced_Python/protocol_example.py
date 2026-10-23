# Python Basics to Advanced Example
# Run: python protocol_example.py

from typing import Protocol

class SupportsArea(Protocol):
    def area(self) -> float: ...

class Circle:
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14159 * self.radius**2

def print_area(shape: SupportsArea): print(shape.area())
print_area(Circle(2))
