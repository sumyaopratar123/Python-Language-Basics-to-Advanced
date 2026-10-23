# Python Basics to Advanced Example
# Run: python class_variable.py

class Employee:
    company = "Example Ltd."
    def __init__(self, name): self.name = name

e = Employee("Ravi")
print(e.name, e.company)
