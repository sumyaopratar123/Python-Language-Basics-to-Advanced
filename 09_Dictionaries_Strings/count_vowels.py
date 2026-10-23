# Python Basics to Advanced Example
# Run: python count_vowels.py

text = input("Text: ").casefold()
print(sum(ch in "aeiou" for ch in text))
