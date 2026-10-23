# Python Basics to Advanced Example
# Run: python palindrome_string.py

text = input("Text: ").casefold()
clean = "".join(ch for ch in text if ch.isalnum())
print("Palindrome" if clean == clean[::-1] else "Not palindrome")
