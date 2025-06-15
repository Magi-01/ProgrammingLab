def countingsort(arr,dec):
    n = len(arr)

    arrx = [0] * 10
    out = [0] * n

    for i in range(0,n):
        index = arr[i] // dec
        arrx[index%10] += 1
    
    for i in range(1,10):
        arrx[i] += arrx[i-1]

    i = n-1
    while i>=0:
        index = arr[i]//dec
        out[arrx[index%10]-1]=arr[i]
        arrx[index%10] -= 1
        i -= 1

    for i in range(0, n):
        arr[i] = out[i]

def radix(arr):
    if len(arr)==0:
        return []
    
    max1 = max(arr)
    exp = 1
    while max1 / exp >= 1:
        countingsort(arr, exp)
        exp *= 10

    return arr

print(radix( [170, 45, 75, 90, 802, 24, 2, 66]))