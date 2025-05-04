graph = {
    'A': [('B', 3), ('C', 1)],
    'B': [('C', 4), ('D', 3)],
    'C': [('D', 5)],
    'D': [('E', 5)],
    'E': [('D', 1)]
}

def dfs(graph, start, node, goal, visited, seted):
    if node in visited:
        return seted.get(node, [None, float('inf')])[1]  # If already visited, return stored distance
    
    visited.add(node)  # Use a set instead of a list for efficiency

    if node == goal:
        return seted[node][1]  # Return the distance to the goal

    min_dist = float('inf')  # Track the minimum distance to goal

    for neighbour, weight in graph.get(node, []):
        if neighbour not in visited:
            seted[neighbour] = [seted[node][0] + [neighbour], seted[node][1] + weight]
            min_dist = min(min_dist, dfs(graph, start, neighbour, goal, visited, seted))

    return min_dist  # Return the shortest distance found


def algo(graph, start, goal):
    visited = set()
    seted = {start: [[start], 0]}  # Ensure path is stored as a list, not a string

    if start == goal:
        return [start], 0  # If start is goal, return immediately

    distance = dfs(graph, start, start, goal, visited, seted)

    return seted[goal][0], distance  # Return the full path and distance


# Example Usage
print(algo(graph, 'A', 'D'))  
