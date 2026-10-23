# Python Basics to Advanced Example
# Run: python linear_search.py

def linear_search(items, target):
    for i, value in enumerate(items):
        if value == target: return i
    return -1

print(linear_search([4, 8, 2, 9], 2))
