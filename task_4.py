import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
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


def heap_draw(nodes):
    heap_root = heap_build(nodes)
    heap = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_edges(heap, heap_root, pos)

    colors = [node[1]["color"] for node in heap.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_build(heap, index=0):
    # heap: Список для побудови купи
    # index: Поточний індекс
    heap = heap_sort(heap)
    if index < len(heap):
        node = Node(heap[index])
        node.left = heap_build(heap, 2 * index + 1)
        node.right = heap_build(heap, 2 * index + 2)
        return node
    return None

def heap_sort(iterable, descending=False):
    # iterable: Вхідний ітерабельний об'єкт
    # descending: вказує, чи потрібно сортувати у зворотньому порядку
    sign = -1 if descending else 1
    heap = [sign * el for el in iterable]
    heapq.heapify(heap)
    return [sign * heapq.heappop(heap) for _ in range(len(heap))]


def main():
    # Несортований список з числами від 1 до 15
    nodes = [2, 9, 13, 1, 10, 6, 4, 7, 14, 12, 5, 8, 15, 11, 3]
    heap_draw(nodes)


if __name__ == "__main__":
    main()
