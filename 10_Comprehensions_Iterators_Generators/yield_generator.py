# Python Basics to Advanced Example
# Run: python yield_generator.py

def even_numbers(limit):
    for n in range(limit+1):
        if n % 2 == 0: yield n

print(list(even_numbers(20)))
