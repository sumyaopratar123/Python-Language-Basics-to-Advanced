# Python Basics to Advanced Example
# Run: python descriptor.py

class Positive:
    def __set_name__(self, owner, name): self.name = "_" + name
    def __get__(self, instance, owner):
        if instance is None: return self
        return getattr(instance, self.name, 0)
    def __set__(self, instance, value):
        if value < 0: raise ValueError("Must be non-negative")
        setattr(instance, self.name, value)

class Product:
    price = Positive()
    def __init__(self, price): self.price = price

print(Product(99).price)
