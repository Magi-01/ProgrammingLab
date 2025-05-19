arr = [13, 36, 60]

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def MCD(arr):
    result = arr[0]
    for i in range(1, len(arr)):
        result = gcd(result, arr[i])
    return result


print(f"MCD of {arr} =", MCD(arr))