# Python Basics to Advanced Example
# Run: python perfect_number.py

def is_perfect(n):
    if n < 2: return False
    total = 1
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            total += d
            if d != n//d: total += n//d
    return total == n

print(is_perfect(28))
