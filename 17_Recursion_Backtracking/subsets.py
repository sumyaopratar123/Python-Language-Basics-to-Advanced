# Python Basics to Advanced Example
# Run: python subsets.py

def subsets(items):
    result = [[]]
    for item in items: result += [subset + [item] for subset in result]
    return result

print(subsets([1, 2, 3]))
