# Python Basics to Advanced Example
# Run: python encapsulation_property.py

class Temperature:
    def __init__(self, celsius): self.celsius = celsius
    @property
    def celsius(self): return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15: raise ValueError("Below absolute zero")
        self._celsius = value

t = Temperature(25)
print(t.celsius)
