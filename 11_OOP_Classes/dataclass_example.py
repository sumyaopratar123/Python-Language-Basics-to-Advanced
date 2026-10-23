# Python Basics to Advanced Example
# Run: python dataclass_example.py

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

print(Point(2, 3))
