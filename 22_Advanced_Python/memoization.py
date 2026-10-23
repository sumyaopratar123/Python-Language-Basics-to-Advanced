# Python Basics to Advanced Example
# Run: python memoization.py

from functools import lru_cache

@lru_cache(maxsize=None)
def ways(n):
    if n < 2: return 1
    return ways(n-1) + ways(n-2)

print(ways(30))
