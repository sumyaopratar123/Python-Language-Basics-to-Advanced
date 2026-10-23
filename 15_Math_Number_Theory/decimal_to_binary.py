# Python Basics to Advanced Example
# Run: python decimal_to_binary.py

n = int(input("Non-negative integer: "))
print(bin(n)[2:] if n >= 0 else "Enter a non-negative integer")
