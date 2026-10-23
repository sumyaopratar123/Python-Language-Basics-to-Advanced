# Python Basics to Advanced Example
# Run: python abstract_class.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2

print(Square(4).area())
