from collections import deque

NAME = "GALLERA"


# ---------------- BINARY TREE ----------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(name):
    """Build the tree level by level (left to right)."""
    nodes = [Node(ch) for ch in name]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def bfs_tree(root):
    """Breadth-First Search using a Queue."""
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def preorder(node):
    """Root -> Left -> Right"""
    return [] if not node else [node.data] + preorder(node.left) + preorder(node.right)


def inorder(node):
    """Left -> Root -> Right"""
    return [] if not node else inorder(node.left) + [node.data] + inorder(node.right)


def postorder(node):
    """Left -> Right -> Root"""
    return [] if not node else postorder(node.left) + postorder(node.right) + [node.data]


# ---------------- GRAPH ----------------
# Duplicate letters are labeled A1, A2, L1, L2.
graph = {
    "G":  ["A1", "L1"],
    "A1": ["G", "L2", "E"],
    "L1": ["G", "R", "A2"],
    "L2": ["A1", "E"],
    "E":  ["A1", "L2"],
    "R":  ["L1", "A2"],
    "A2": ["L1", "R"],
}


def bfs_graph(graph, start):
    """Breadth-First Search using a Queue."""
    visited, queue, result = {start}, deque([start]), []
    while queue:
        v = queue.popleft()
        result.append(v)
        for neighbor in graph[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def dfs_graph(graph, v, visited=None):
    """Depth-First Search using recursion (the call stack)."""
    if visited is None:
        visited = []
    visited.append(v)
    for neighbor in graph[v]:
        if neighbor not in visited:
            dfs_graph(graph, neighbor, visited)
    return visited


# ---------------- RUN ----------------
if __name__ == "__main__":
    root = build_tree(NAME)

    print("BINARY TREE:", NAME)
    print("BFS (Level-order):", " -> ".join(bfs_tree(root)))
    print("DFS Preorder     :", " -> ".join(preorder(root)))
    print("DFS Inorder      :", " -> ".join(inorder(root)))
    print("DFS Postorder    :", " -> ".join(postorder(root)))

    print("\nGRAPH:", NAME)
    print("BFS:", " -> ".join(bfs_graph(graph, "G")))
    print("DFS:", " -> ".join(dfs_graph(graph, "G")))