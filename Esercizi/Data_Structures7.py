# Given
# (A, B): 1
# (A, C): 4
# (B, C): 2
# (B, D): 6
# (C, D): 3
# Find the distance from a to all other nodes using dijkistra
from collections import deque

def build_adjacency_list(edges):
    adjacency = {}

    for (u, v), weight in edges.items():
        if u not in adjacency:
            adjacency[u] = set()
        adjacency[u].add((v, weight))  # Using a set to ensure uniqueness

        if v not in adjacency:
            adjacency[v] = set()

    return adjacency

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    paths = {node: [] for node in graph}
    paths[start] = [start]

    queue = deque(graph.keys())  # Nodes to visit

    while queue:
        node = min(queue, key=lambda node: distances[node])  # Get min node manually
        queue.remove(node)


        for neighbor, weight in graph[node]:
            new_distance = distances[node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                paths[neighbor] = paths[node] + [neighbor]

    return distances, paths

def solve(lis, start):
    if len(lis) == 1:
        return lis.values()
    
    adjacency = build_adjacency_list(lis)

    return dijkstra(adjacency, start)

lis = {
    ('A', 'B'): 1,
    ('A', 'C'): 1,
    ('B', 'C'): 1,
    ('B', 'D'): 5,
    ('C', 'D'): 1
}

print(solve(lis, 'A'))

