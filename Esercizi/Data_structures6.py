# Array A[1,...,n] of only 1 and 0, not ordered but can be all the same, order the array in ascending and use two pointers

def solve(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        if arr[left] < arr[right]:
            right -= 1
        else:
            left += 1
    return arr

arr = [1,0,1,0,1,0,1,1,1,0]
print(solve(arr))