# Python Basics to Advanced Example
# Run: python inheritance.py

class Animal:
    def speak(self): return "Some sound"
class Dog(Animal):
    def speak(self): return "Woof"

print(Dog().speak())
