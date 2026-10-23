# Python Basics to Advanced Example
# Run: python binary_tree_inorder.py

class Node:
    def __init__(self, value, left=None, right=None): self.value, self.left, self.right = value, left, right

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

root = Node(2, Node(1), Node(3))
inorder(root)
print()
