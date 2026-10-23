# Python Basics to Advanced Example
# Run: python graph_dfs.py

def dfs(graph, start):
    visited, order = set(), []
    def visit(node):
        if node in visited: return
        visited.add(node); order.append(node)
        for neighbor in graph.get(node, []): visit(neighbor)
    visit(start)
    return order

graph = {"A":["B","C"], "B":["D"], "C":["D"], "D":[]}
print(dfs(graph, "A"))
