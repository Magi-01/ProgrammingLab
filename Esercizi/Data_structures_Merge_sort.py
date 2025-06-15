arr = [2,3,4,-5,1]

# Merge sort sorts a list by;
# Dividing the list in half untill the dimension is <= 1 after which recostructs the list while ordering using Merge:
#  iterates through the length of the right sub-array and left sub-array:
#   if the value of the left subarray is larger than the right, append the 
#   right add add it's step otherwise do same for left. At the end add all the 
#   values that remain if the step for one of the subarrays stopped earlier 
#   than the other


# Time Complexity O(nlog(n))
# Space Complexity O(1)

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

def merge_inplace(arr, left, mid, right):
    
    n1 = mid - left + 1
    n2 = right - mid
    
    # Create temporary lists 
    # for left and right subarrays
    arr1 = arr[left:left + n1]
    arr2 = arr[mid + 1:mid + 1 + n2]
    
    i = 0    
    j = 0    
    k = left 
    
    # Merge the temp lists back into arr
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    
    # Copy remaining elements of arr1[] if any
    while i < n1:
        arr[k] = arr1[i]
        i += 1
        k += 1
    
    # Copy remaining elements of arr2[] if any
    while j < n2:
        arr[k] = arr2[j]
        j += 1
        k += 1


def merge_sort_inplace(arr):
    n = len(arr)
    
    # Iterate through subarrays of increasing size
    currSize = 1
    while currSize <= n - 1:
        
        # Pick starting points of different
        # subarrays of current size
        leftStart = 0
        while leftStart < n - 1:
            
            # Find endpoints of the subarrays to be merged
            mid = min(leftStart + currSize - 1, n - 1)
            rightEnd = min(leftStart + 2 * currSize - 1, n - 1)
            
            # Merge the subarrays arr[leftStart...mid]
            # and arr[mid+1...rightEnd]
            merge_inplace(arr, leftStart, mid, rightEnd)
            
            leftStart += 2 * currSize

        currSize = 2 * currSize

print(merge_sort(arr))
arr = [2,3,4,-5,1]
merge_sort_inplace(arr)
print(arr)