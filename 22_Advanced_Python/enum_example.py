# Python Basics to Advanced Example
# Run: python enum_example.py

from enum import Enum, auto

class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()

print(Status.RUNNING.name, Status.RUNNING.value)
