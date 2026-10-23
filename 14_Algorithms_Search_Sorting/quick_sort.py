# Python Basics to Advanced Example
# Run: python quick_sort.py

def quick_sort(items):
    if len(items) < 2: return items[:]
    pivot = items[len(items)//2]
    return quick_sort([x for x in items if x < pivot]) + [x for x in items if x == pivot] + quick_sort([x for x in items if x > pivot])

print(quick_sort([8, 3, 1, 7, 0, 10, 2]))
