# Python Basics to Advanced Example
# Run: python reverse_number.py

n = int(input("Integer: "))
sign = -1 if n < 0 else 1
print(sign * int(str(abs(n))[::-1]))
