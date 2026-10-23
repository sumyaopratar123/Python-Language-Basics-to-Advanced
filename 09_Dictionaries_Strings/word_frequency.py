# Python Basics to Advanced Example
# Run: python word_frequency.py

text = "python is fun and python is useful"
counts = {}
for word in text.split(): counts[word] = counts.get(word, 0) + 1
print(counts)
