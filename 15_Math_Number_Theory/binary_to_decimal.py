# Python Basics to Advanced Example
# Run: python binary_to_decimal.py

binary = input("Binary digits: ")
if binary and set(binary) <= {"0", "1"}: print(int(binary, 2))
else: print("Invalid binary number")
