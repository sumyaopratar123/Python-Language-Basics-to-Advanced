# Python Basics to Advanced Example
# Run: python merge_sorted_lists.py

def merge_sorted(a, b):
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]: result.append(a[i]); i += 1
        else: result.append(b[j]); j += 1
    return result + a[i:] + b[j:]

print(merge_sorted([1, 3, 8], [2, 4, 7]))
