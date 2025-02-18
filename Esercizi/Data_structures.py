"""def fib(n, visited=None):
    if visited is None:
        visited = {}
    if n <= 2:
        return 1
    if n not in visited:
        visited[n] = fib(n-1) + fib(n-2)
    return visited[n]
print(fib(17))"""

"""import numpy as np

def longestsub(a,b):
    n = len(a)
    m = len(b)
    lc = np.zeros((n+1, m+1))

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]: # Se il carattere in posizione i,j coincide
                lc[i][j] = 1 + lc[i-1][j-1]
            else: # altrimenti prendiamo il migliore dei due sottoproblemi
                lc[i][j] = max(lc[i-1][j], lc[i][j-1])
    return lc[n][m]


a = "CASSSA"
b = "ASSICURAZIONE"
a = list(a)
b = list(b)
print(a,b)
print(longestsub(a,b))"""

def travelling_salesman(w,maxW):
    count += 1
    k = 0
    visited = {}
    for i in range(len(w)-1):
        for j in range(i+1, len(w)):
            visited[j] = max(visited[j-1]+w[i],visited[j-1]+w[i+1])
        if visited[i] <= maxW:
            maxW = maxW - k
            count += 1