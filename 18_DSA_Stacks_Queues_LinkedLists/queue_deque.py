# Python Basics to Advanced Example
# Run: python queue_deque.py

from collections import deque

queue = deque([1, 2, 3])
queue.append(4)
print("served:", queue.popleft())
print(list(queue))
