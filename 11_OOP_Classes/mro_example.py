# Python Basics to Advanced Example
# Run: python mro_example.py

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
print([cls.__name__ for cls in D.mro()])
