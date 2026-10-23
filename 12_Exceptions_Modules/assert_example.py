# Python Basics to Advanced Example
# Run: python assert_example.py

def percentage(value):
    assert 0 <= value <= 100, "Value must be between 0 and 100"
    return value

print(percentage(85))
