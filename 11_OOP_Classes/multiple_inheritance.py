# Python Basics to Advanced Example
# Run: python multiple_inheritance.py

class Flyer:
    def fly(self): return "Flying"
class Swimmer:
    def swim(self): return "Swimming"
class Duck(Flyer, Swimmer): pass

d = Duck()
print(d.fly(), d.swim())
