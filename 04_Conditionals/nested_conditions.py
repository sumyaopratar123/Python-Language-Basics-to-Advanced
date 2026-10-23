# Python Basics to Advanced Example
# Run: python nested_conditions.py

age = int(input("Age: "))
if age >= 18:
    has_license = input("Have license? (yes/no): ").lower() == "yes"
    print("Can drive" if has_license else "Need a license")
else: print("Too young to drive")
