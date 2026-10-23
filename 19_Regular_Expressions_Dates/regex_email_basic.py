# Python Basics to Advanced Example
# Run: python regex_email_basic.py

import re

email = input("Email: ").strip()
pattern = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
print("Looks like an email" if re.match(pattern, email) else "Invalid format")
print("Note: real email validation is more complex.")
