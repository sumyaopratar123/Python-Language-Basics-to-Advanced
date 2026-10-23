# Python Basics to Advanced Example
# Run: python expense_tracker.py

expenses = []
while True:
    value = input("Expense amount (or q): ").strip()
    if value.lower() == "q": break
    try:
        amount = float(value)
        if amount < 0: raise ValueError
        category = input("Category: ").strip() or "Other"
        expenses.append((category, amount))
    except ValueError: print("Enter a non-negative number.")
print("Total:", sum(amount for _, amount in expenses))
for category, amount in expenses: print(category, amount)
