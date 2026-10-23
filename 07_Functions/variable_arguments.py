# Python Basics to Advanced Example
# Run: python variable_arguments.py

def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))
