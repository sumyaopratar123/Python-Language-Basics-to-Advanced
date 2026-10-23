# Python Basics to Advanced Example
# Run: python regex_extract_numbers.py

import re

text = "Order 42 contains 3 items and costs 1200 rupees."
print(re.findall(r"\d+", text))
