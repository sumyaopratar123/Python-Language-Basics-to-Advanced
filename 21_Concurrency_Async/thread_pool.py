# Python Basics to Advanced Example
# Run: python thread_pool.py

from concurrent.futures import ThreadPoolExecutor

def square(n): return n*n

with ThreadPoolExecutor(max_workers=3) as pool:
    print(list(pool.map(square, range(10))))
