arr = [-4,1,2,3,4,5,6,36,40]

def binary(arr, n, k):
    left, right = 1, n

    while right > 1:
        mid = (left + right) // 2

        if arr[mid] == k:
            return k
        
        if arr[mid] < k:
            left = mid
        else:
            right = mid
            
    return "Not found"

print(binary(arr, len(arr), 40))