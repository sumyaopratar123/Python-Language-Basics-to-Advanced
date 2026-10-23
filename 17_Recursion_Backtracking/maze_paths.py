# Python Basics to Advanced Example
# Run: python maze_paths.py

def paths(r, c):
    if r == 1 or c == 1: return 1
    return paths(r-1, c) + paths(r, c-1)

print(paths(4, 4))
