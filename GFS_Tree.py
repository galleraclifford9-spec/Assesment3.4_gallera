NAME = "GALLERA"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(name):
    nodes = [Node(ch) for ch in name]
    for i, node in enumerate(nodes):
        left, right = 2 * i + 1, 2 * i + 2
        if left < len(nodes):
            node.left = nodes[left]
        if right < len(nodes):
            node.right = nodes[right]
    return nodes[0]


def preorder(node):
    return [] if not node else [node.data] + preorder(node.left) + preorder(node.right)


def inorder(node):
    return [] if not node else inorder(node.left) + [node.data] + inorder(node.right)


def postorder(node):
    return [] if not node else postorder(node.left) + postorder(node.right) + [node.data]


if __name__ == "__main__":
    root = build_tree(NAME)

    print("BINARY TREE:", NAME)
    print("DFS Preorder     :", " -> ".join(preorder(root)))
    print("DFS Inorder      :", " -> ".join(inorder(root)))
    print("DFS Postorder    :", " -> ".join(postorder(root)))