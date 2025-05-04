def knapsack(maximum, items, weights, n, visited):
    if maximum == 0 or n == 0:
        return 0, []
    
    if (maximum, n) in visited:
        return visited[(maximum, n)]

    if weights[n - 1] > maximum:
        result = knapsack(maximum, items, weights, n - 1, visited)
        visited[(maximum, n)] = result  # Store result for this subproblem
        return result
    
    include_weight, include_items = knapsack(maximum - weights[n - 1], items, weights, n - 1, visited)
    exclude_weight, exclude_items = knapsack(maximum, items, weights, n - 1, visited)

    if weights[n - 1] + include_weight > exclude_weight:
        result = (weights[n - 1] + include_weight, include_items + [items[n - 1]])
    else:
        result = (exclude_weight, exclude_items)

    visited[(maximum, n)] = result  # Store result for this subproblem
    return result

def solve(maximum, items, weights, n):
    visited = {}
    return knapsack(maximum, items, weights, n, visited)


maximum = 50
items = ['A', 'B', 'C']
weights = [6, 5, 4]
print(solve(maximum, items, weights, len(items)))