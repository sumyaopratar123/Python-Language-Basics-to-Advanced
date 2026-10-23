# Python Basics to Advanced Example
# Run: python merge_sort.py

def merge_sort(items):
    if len(items) <= 1: return items[:]
    mid = len(items)//2
    left, right = merge_sort(items[:mid]), merge_sort(items[mid:])
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    return result + left + right

print(merge_sort([7, 2, 9, 1, 5]))
