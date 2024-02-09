import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#59074f"):
        self.left = None
        self.right = None
        self.val = key
        self.base_color = color
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def dfs(node, visited, base_color):
    if node is not None:
        visited.add(node.id)
        node.color = get_color(base_color, len(visited))
        dfs(node.left, visited, base_color)
        dfs(node.right, visited, base_color)


def bfs(root, base_color):
    if root is not None:
        visited = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.id not in visited:
                visited.add(node.id)
                node.color = get_color(base_color, len(visited))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


def get_color(base_color, index):
    base_rgb = tuple(int(base_color.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
    step = 15
    new_rgb = tuple(min(255, c + index * step) for c in base_rgb)
    return "#{:02X}{:02X}{:02X}".format(*new_rgb)

def main():
    root = Node(10)

    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.left.left.left = Node(2)
    root.left.left.right = Node(4)
    root.left.right.left = Node(6)
    root.left.right.right = Node(8)

    root.right = Node(15)
    root.right.left = Node(13)
    root.right.right = Node(17)
    root.right.left.left = Node(12)
    root.right.left.right = Node(14)
    root.right.right.left = Node(16)
    root.right.right.right = Node(18)

    draw_tree(root)

    dfs(root, set(), root.base_color)
    draw_tree(root)

    bfs(root, root.base_color)
    draw_tree(root) 


if __name__ == "__main__":
    main()