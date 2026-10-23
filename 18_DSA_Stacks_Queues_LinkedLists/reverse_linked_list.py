# Python Basics to Advanced Example
# Run: python reverse_linked_list.py

class Node:
    def __init__(self, value, next_node=None): self.value, self.next = value, next_node

def reverse(head):
    previous = None
    while head:
        following = head.next
        head.next = previous
        previous, head = head, following
    return previous

head = Node(1, Node(2, Node(3)))
new_head = reverse(head)
while new_head:
    print(new_head.value, end=" ")
    new_head = new_head.next
