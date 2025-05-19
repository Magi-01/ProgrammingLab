arr = [2,3,4,-5,1]

def selection(arr, n):
    right = n-1
    while right > 0:
        left = 0
        while left < right:
            if arr[left] > arr[right]:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
            left += 1
        temp = arr[right]
        arr[right] = arr[max]
        arr[max] = temp
        right -= 1
    return arr

print(selection(arr, len(arr)))