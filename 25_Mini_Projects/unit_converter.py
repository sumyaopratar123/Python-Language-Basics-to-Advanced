# Python Basics to Advanced Example
# Run: python unit_converter.py

print("1 km to miles | 2 Celsius to Fahrenheit | 3 kg to pounds")
choice = input("Choice: ").strip()
value = float(input("Value: "))
if choice == "1": print(value * 0.621371)
elif choice == "2": print(value * 9/5 + 32)
elif choice == "3": print(value * 2.20462)
else: print("Invalid choice")
