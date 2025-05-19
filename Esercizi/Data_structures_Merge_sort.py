arr = [2,3,4,-5,1]

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    arr1 = arr[:mid]
    arr2 = arr[mid:]
    sortedLeft = merge_sort(arr1)
    sortedRight = merge_sort(arr2)

    return merge(sortedLeft, sortedRight)

print(merge_sort(arr))