# Python Basics to Advanced Example
# Run: python triangle_type.py

a, b, c = sorted(map(float, input("Three sides: ").split()))
if a+b <= c: print("Invalid triangle")
elif a == c: print("Equilateral")
elif a == b or b == c: print("Isosceles")
else: print("Scalene")
