# Python Basics to Advanced Example
# Run: python rotate_list.py

items = [1, 2, 3, 4, 5]
k = 2
k %= len(items)
print(items[-k:] + items[:-k])
