# Insertion sort has a complexity of O(n^2)

arr = [2,3,4,-5,1]

def insertion(arr, n):
    for i in range(2, n):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

print(insertion(arr, len(arr)))