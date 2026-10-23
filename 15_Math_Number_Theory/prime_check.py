# Python Basics to Advanced Example
# Run: python prime_check.py

import math

def is_prime(n):
    if n < 2: return False
    for d in range(2, math.isqrt(n)+1):
        if n % d == 0: return False
    return True

print(is_prime(29))
