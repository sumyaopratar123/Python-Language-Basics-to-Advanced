# Python Basics to Advanced Example
# Run: python recursive_binary_search.py

def search(a, target, lo=0, hi=None):
    if hi is None: hi = len(a)-1
    if lo > hi: return -1
    mid = (lo+hi)//2
    if a[mid] == target: return mid
    if a[mid] < target: return search(a, target, mid+1, hi)
    return search(a, target, lo, mid-1)

print(search([2, 4, 6, 8, 10], 8))
