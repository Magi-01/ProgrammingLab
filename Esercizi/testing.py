def ALGO(c,t,T, memo):
    if T<=0:
        return 0
    
    max_cost = 0
    
    if T in memo:
         return memo[T]
    
    for i in range(len(t)):
        if T - t[i] >= 0:
            cost = c[i] + ALGO(c,t,T-t[i], memo)
            max_cost = max(max_cost, cost)

    memo[T] = max_cost
    return max_cost
    
c = [500,400,20,10]
t = [2,5,6,10]
T = 10
memo = {}
print(ALGO(c,t,T, memo))
