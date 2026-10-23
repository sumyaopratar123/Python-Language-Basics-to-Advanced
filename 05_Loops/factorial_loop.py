# Python Basics to Advanced Example
# Run: python factorial_loop.py

n = int(input("Non-negative integer: "))
result = 1
if n < 0: print("Invalid input")
else:
    for i in range(2, n+1): result *= i
    print(result)
