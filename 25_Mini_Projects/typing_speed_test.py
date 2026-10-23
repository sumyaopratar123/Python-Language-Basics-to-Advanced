# Python Basics to Advanced Example
# Run: python typing_speed_test.py

import time

phrase = "Python practice makes programming easier."
print("Type this exactly:", phrase)
start = time.perf_counter()
entered = input("> ")
elapsed = max(time.perf_counter()-start, 0.001)
words = len(entered.split())
print(f"Time: {elapsed:.2f}s | Speed: {words/(elapsed/60):.1f} WPM")
print("Exact match:", entered == phrase)
