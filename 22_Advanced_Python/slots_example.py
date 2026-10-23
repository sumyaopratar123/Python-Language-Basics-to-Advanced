# Python Basics to Advanced Example
# Run: python slots_example.py

class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y

p = Point(2, 4)
print(p.x, p.y)
