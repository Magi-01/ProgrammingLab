# list A of k doubles A[[2],...,[2]] wher b implies a, find all copies where a imples b and b implies a
# A -> B <==> B -> A

def algo(node, dict_arr, visited, path):
    if node in visited:
        if visited[node] == "visiting":
            return False
        return True
    
    visited[node] = "visiting"

    for neighbour in dict_arr[node]:
        if neighbour in visited:
            if visited[neighbour] == "visiting":
                return False
            
        if neighbour not in visited:
            return algo(neighbour, dict_arr, visited, path)
        
        path.append(neighbour)
    
    visited[node] = "visited"
    return True

def check(arr):
    if len(arr) < 2:
        return True
    
    visited = {}
    dict_arr = {}
    
    for node in arr:
        left = node[0]
        right = node[1] if len(node) > 1 else None
        if left not in dict_arr:
            dict_arr[left] = []
        if right is not None:
            if right not in dict_arr:
                dict_arr[right] = []
            dict_arr[left].append(right)

    path = []

    for node in dict_arr:
        path.append(node)
        if node not in visited:
            if not algo(node, dict_arr, visited, path):
                return False
    
    return True, path


arr = [
    ['M','A'],
    ['M','D'],
    ['A','D'],
    ['D','C'],
    ['D','E'],
    ['C'],
    ['E']
]
print(check(arr))