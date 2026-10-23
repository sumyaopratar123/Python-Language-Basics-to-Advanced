# Python Basics to Advanced Example
# Run: python balanced_parentheses.py

def balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in text:
        if ch in "([{": stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]: return False
    return not stack

print(balanced("{[()]}"))
