def DFS(A):
    visited = {node: 0 for node in A}

    for s in A:
        if visited[s] == 0:
            stack = [(s, 0)]
            visited[s] = 1  # Mark as visiting

            while stack:
                current, idx  = stack.pop()
                neighbors = A[current]

                if idx < len(neighbors):
                    neighbor = neighbors[idx]
                    stack.append((current, idx + 1))

                    if visited[neighbor] == 0:
                        visited[neighbor] = 1
                        stack.append((neighbor, 0))
                    elif visited[neighbor] == 1:
                        return "cyclic"  # Found a back edge
                else:
                    visited[current] = 2  # done visiting
                    stack.pop()
    return "Not cyclic"


arr = {
    'A': ['B', 'D'],
    'B': ['C', 'D'],
    'C': ['A'],
    'D': [],
}

print(DFS(arr))