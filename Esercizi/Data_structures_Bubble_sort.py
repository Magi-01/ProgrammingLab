arr = [2,3,4,-5,1]

def bubble(arr, n):
    right = n-1
    max = float('-inf')
    while right > 0:
        left = 0
        while left < right:
            if arr[left] > max:
                max = left
            left += 1
        temp = arr[right]
        arr[right] = arr[max]
        arr[max] = temp
        right -= 1
    return arr

print(bubble(arr, len(arr)))