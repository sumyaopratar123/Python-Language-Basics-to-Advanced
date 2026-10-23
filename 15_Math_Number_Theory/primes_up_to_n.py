# Python Basics to Advanced Example
# Run: python primes_up_to_n.py

def primes_up_to(n):
    sieve = [True] * (n+1)
    if n >= 0: sieve[0] = False
    if n >= 1: sieve[1] = False
    for p in range(2, int(n**0.5)+1):
        if sieve[p]:
            for multiple in range(p*p, n+1, p): sieve[multiple] = False
    return [i for i, ok in enumerate(sieve) if ok]

print(primes_up_to(50))
