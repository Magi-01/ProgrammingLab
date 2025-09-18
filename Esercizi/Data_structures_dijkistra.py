import heapq

def dijkistra(A,s):
    visited = set()

    matrix = {}
    for i in A:
        matrix[i] = {}
        for j, w in A[i]:
            matrix[i][j] = w
    
    dist = {node: float('inf') for node in matrix}
    dist[s] = 0

    heap = [(0,s)]

    while heap:
        d, node = heapq.heappop(heap)
        if node not in visited:
            visited.add(node)

            for v, _ in A[node]:
                if matrix[node][v]!=0 and v not in visited:
                     new_dist = d + matrix[node][v]
                     if new_dist < dist[v]:
                          dist[v] = new_dist
                          heapq.heappush(heap, (new_dist,v))
                     
    return dist


arr = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}

print(dijkistra(arr,'A'))