# Python Basics to Advanced Example
# Run: python threading_demo.py

import threading

def worker(name): print(f"Worker {name} is running")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for thread in threads: thread.start()
for thread in threads: thread.join()
