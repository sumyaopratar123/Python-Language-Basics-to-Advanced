# Python Basics to Advanced Example
# Run: python linked_list.py

class Node:
    def __init__(self, value, next_node=None):
        self.value, self.next = value, next_node

head = Node(1, Node(2, Node(3)))
current = head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
