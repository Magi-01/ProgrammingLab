arr = [1,13,4,-1,10,5,20,11,9,12]
k = 7

def merge(l,r):
    result = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result.extend(l[i:])
    result.extend(r[j:])

    return result

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr

    mid = n//2

    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])

    return merge(l,r)

def fun(arr, k):
    arr2 = merge_sort(arr)
    print(arr2)
    n = len(arr2)
    left = 0
    right = n-1

    while left < right:
        if arr2[left] + arr2[right] == k:
            return True
        if arr2[left] + arr2[right] < k:
            left += 1
        if arr2[left] + arr2[right] > k:
            right -= 1
    return False

    

print(fun(arr,k))