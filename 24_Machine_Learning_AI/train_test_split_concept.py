# Python Basics to Advanced Example
# Run: python train_test_split_concept.py

from random import Random

rng = Random(42)
data = list(range(20))
rng.shuffle(data)
split = int(len(data) * 0.8)
train, test = data[:split], data[split:]
print("Train:", train)
print("Test:", test)
