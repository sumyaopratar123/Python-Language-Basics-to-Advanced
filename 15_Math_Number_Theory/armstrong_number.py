# Python Basics to Advanced Example
# Run: python armstrong_number.py

n = int(input("Integer: "))
digits = str(abs(n))
print("Armstrong" if n >= 0 and sum(int(d)**len(digits) for d in digits) == n else "Not Armstrong")
