# Python Basics to Advanced Example
# Run: python anagram_check.py

a = input("First word: ").replace(" ", "").casefold()
b = input("Second word: ").replace(" ", "").casefold()
print("Anagrams" if sorted(a) == sorted(b) else "Not anagrams")
