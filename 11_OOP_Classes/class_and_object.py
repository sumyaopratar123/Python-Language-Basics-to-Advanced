# Python Basics to Advanced Example
# Run: python class_and_object.py

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self): print(self.name, self.marks)

Student("Asha", 92).display()
