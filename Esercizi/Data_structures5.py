# money in an array A[1,...,n], we want to use the max amount of coins

def pay_repeating(arr, maxim, n, visited):
    if maxim < 0:
        return 0
    if n == 0:
        return 0
    
    if (maxim,n) in visited:
        return visited[(maxim,n)]

    if arr[n - 1] <= maxim:
        choose_coin = 1 + pay_repeating(arr, round(maxim - arr[n - 1], 3), n, visited)
    else:
        choose_coin = 0
        
    skip_coin = pay_repeating(arr, maxim, n-1, visited)

    best = max(choose_coin, skip_coin)
    visited[(maxim,n)] = best

    return best

def summ(arr, maxim, n, visited):
    if maxim == 0 or n == 0:
        return 0
    
    if (maxim,n) in visited:
        return visited[(maxim,n)]

    if arr[n - 1] <= maxim:
        choose_coin = arr[n - 1] + summ(arr, round(maxim - arr[n - 1], 3), n-1, visited)
    else:
        choose_coin = 0
        
    skip_coin = summ(arr, maxim, n-1, visited)

    best = max(choose_coin, skip_coin)

    visited[(maxim,n)] = best

    return best

def algo(arr, maxim):
    n = len(arr)

    if n==0:
        return 0
    if n == 1:
        return int(maxim//arr)
    
    visited = {}
    visited1 = {}

    seted = pay_repeating(arr, maxim, n, visited)
    seted1 = summ(arr, maxim, n, visited1)

    return seted, seted1

arr = [5,6.11]
maxim = 11.11

print(algo(arr, maxim))