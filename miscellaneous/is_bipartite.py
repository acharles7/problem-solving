def isBipartite(graph) -> bool:
    color = {}
    for node in range(len(graph)):
        if node not in color:
            stack = [node]
            color[node] = 0
            while stack:
                node = stack.pop()
                for neighbour in graph[node]:
                    if neighbour not in color:
                        stack.append(neighbour)
                        color[neighbour] = color[node] ^ 1
                    elif color[neighbour] == color[node]:
                        return False
    return True


graph = [[1, 3], [0, 2], [1, 3], [0, 2]]
print(isBipartite(graph))
