import heapq

def dijkistra_path(A, s, f):
    visited = set()
    prev = {}
    matrix = {}

    for i in A:
        matrix[i] = {}
        for j, w in A[i]:
            matrix[i][j] = w
    
    dist = {node: float('inf') for node in A}
    dist[s] = 0

    heap = [(0, s)]

    while heap:
        d, node = heapq.heappop(heap)
        if node == f:
            path = []
            while node in prev:
                path.append(node)
                node = prev[node]
            path.append(s)
            path.reverse()
            return dist, path
        
        if node not in visited:
            visited.add(node)

            for v, _ in A[node]:
                if v not in visited:
                     new_dist = d + matrix[node][v]
                     if new_dist < dist[v]:
                        dist[v] = new_dist
                        prev[v] = node
                        heapq.heappush(heap, (new_dist, v))
    return 'no path'
                     
    


arr = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}

print(dijkistra_path(arr,'A', 'D'))