# Python Basics to Advanced Example
# Run: python classmethod_staticmethod.py

class Converter:
    @staticmethod
    def km_to_miles(km): return km * 0.621371
    @classmethod
    def unit_name(cls): return "distance converter"

print(Converter.km_to_miles(5), Converter.unit_name())
