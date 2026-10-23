# Python Basics to Advanced Example
# Run: python insertion_sort.py

def insertion_sort(items):
    a = items[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

print(insertion_sort([9, 5, 1, 4, 3]))
