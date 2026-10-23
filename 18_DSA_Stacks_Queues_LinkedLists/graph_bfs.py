# Python Basics to Advanced Example
# Run: python graph_bfs.py

from collections import deque

def bfs(graph, start):
    visited, queue, order = {start}, deque([start]), []
    while queue:
        node = queue.popleft(); order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor); queue.append(neighbor)
    return order

graph = {"A":["B","C"], "B":["D"], "C":["D"], "D":[]}
print(bfs(graph, "A"))
