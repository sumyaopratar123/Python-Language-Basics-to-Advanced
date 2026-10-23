# Python Basics to Advanced Example
# Run: python triangle_validity.py

a, b, c = map(float, input("Three sides: ").split())
print("Valid triangle" if a+b>c and a+c>b and b+c>a else "Invalid triangle")
