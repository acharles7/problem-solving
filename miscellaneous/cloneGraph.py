"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

def cloneGraph(node: 'Node') -> 'Node':
    if not node: return node

    graph = defaultdict(Node)
    graph[node] = Node(node.val, [])
    queue = [node]


    while queue:
        last = queue.pop(0)
        value, neighbours = last.val, last.neighbors

        for neighbour in neighbours:
            if neighbour not in graph:
                graph[neighbour] = Node(neighbour.val, [])
                queue.append(neighbour)
            graph[last].neighbors.append(graph[neighbour])

    return graph[node]

