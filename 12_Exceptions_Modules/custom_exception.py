# Python Basics to Advanced Example
# Run: python custom_exception.py

class InsufficientBalanceError(Exception): pass

def withdraw(balance, amount):
    if amount > balance: raise InsufficientBalanceError("Insufficient funds")
    return balance - amount

print(withdraw(1000, 250))
