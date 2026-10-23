# Python Basics to Advanced Example
# Run: python character_frequency.py

from collections import Counter
text = input("Text: ").replace(" ", "")
print(Counter(text))
