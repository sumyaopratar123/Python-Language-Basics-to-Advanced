# Python Basics to Advanced Example
# Run: python closure_example.py

def make_multiplier(factor):
    def multiply(value): return value * factor
    return multiply

double = make_multiplier(2)
print(double(9))
