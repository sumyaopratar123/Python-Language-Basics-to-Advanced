# Python Basics to Advanced Example
# Run: python password_generator.py

import secrets
import string

length = int(input("Password length (8+ recommended): "))
if length < 1: print("Length must be positive")
else:
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_"
    print("".join(secrets.choice(alphabet) for _ in range(length)))
