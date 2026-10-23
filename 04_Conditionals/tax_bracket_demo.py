# Python Basics to Advanced Example
# Run: python tax_bracket_demo.py

income = float(input("Annual income: "))
if income < 0: print("Invalid income")
elif income < 300000: print("Example bracket: low")
elif income < 700000: print("Example bracket: medium")
else: print("Example bracket: high")
print("Educational example only; not tax advice.")
