# Python Basics to Advanced Example
# Run: python invert_dictionary.py

data = {"a": 1, "b": 2, "c": 1}
inverted = {}
for key, value in data.items(): inverted.setdefault(value, []).append(key)
print(inverted)
