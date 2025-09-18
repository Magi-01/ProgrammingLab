from collections import deque

def is_connected(dist):
    return float('inf') in dist.values()

def BFS(A,s):
    visited = set()
    dist = {node: float('inf') for node in A}
    dist[s] = 0
    queue = deque()
    queue.append((dist[s], s))

    while queue:
        d, node = queue.popleft()
        if node not in visited:
            visited.add(node)

            for v in A[node]:
                if v not in visited:
                    new_dist = d + 1
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        queue.append((dist[v], v))
    
    flag = is_connected(dist)
    return dist, flag


arr = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': [],
    'Z': []
}

print(BFS(arr,'A'))