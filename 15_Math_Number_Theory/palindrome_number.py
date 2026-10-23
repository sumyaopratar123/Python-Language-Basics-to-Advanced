# Python Basics to Advanced Example
# Run: python palindrome_number.py

n = input("Integer: ").strip()
print("Palindrome" if n.lstrip("-") == n.lstrip("-")[::-1] else "Not palindrome")
