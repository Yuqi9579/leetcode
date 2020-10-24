graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}#定义一个无向图

def BFS(graph, start):
    visited = set(start)
    queue = []
    queue.append(start)
    for i in range(len(graph)):
        vertex = queue.pop(0)
        print(vertex)
        for neib in graph[vertex]:
            if neib not in visited:
                visited.add(neib)
                queue.append(neib)


BFS(graph, 'B')