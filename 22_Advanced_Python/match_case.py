# Python Basics to Advanced Example
# Run: python match_case.py

def describe(value):
    match value:
        case 0: return "zero"
        case 1: return "one"
        case _: return "many or another value"

print(describe(3))
