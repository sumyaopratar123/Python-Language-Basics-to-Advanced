# Python Basics to Advanced Example
# Run: python two_sum.py

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target-n in seen: return [seen[target-n], i]
        seen[n] = i
    return []

print(two_sum([2, 7, 11, 15], 9))
