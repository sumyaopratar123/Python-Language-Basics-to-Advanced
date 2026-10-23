# Python Basics to Advanced Example
# Run: python try_except.py

try:
    number = int(input("Integer: "))
    print(100 / number)
except ValueError:
    print("Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
