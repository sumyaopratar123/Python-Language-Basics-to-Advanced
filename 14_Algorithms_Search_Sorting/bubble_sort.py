# Python Basics to Advanced Example
# Run: python bubble_sort.py

def bubble_sort(items):
    a = items[:]
    for end in range(len(a)-1, 0, -1):
        swapped = False
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True
        if not swapped: break
    return a

print(bubble_sort([5, 1, 4, 2, 8]))
