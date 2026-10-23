# Python Basics to Advanced Example
# Run: python pythagorean_triplet.py

a, b, c = sorted(map(int, input("Three integers: ").split()))
print("Pythagorean triplet" if a*a+b*b == c*c else "Not a Pythagorean triplet")
