# Python Basics to Advanced Example
# Run: python selection_sort.py

def selection_sort(items):
    a = items[:]
    for i in range(len(a)):
        smallest = min(range(i, len(a)), key=a.__getitem__)
        a[i], a[smallest] = a[smallest], a[i]
    return a

print(selection_sort([64, 25, 12, 22, 11]))
