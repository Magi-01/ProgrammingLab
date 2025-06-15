arr = [1,3,5,7,9]
arr2 = [2,4,6,8,10]

def heapify(arr,i,n):
     # Initialize largest as root
    largest = i 
    
    #  left index = 2*i + 1
    l = 2 * i + 1 
    
    # right index = 2*i + 2
    r = 2 * i + 2

    # If left child is larger than root
    if l < n and arr[l] < arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] < arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, largest, n)


def heap(arr,arr2,n):
    result = []

    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
        heapify(arr2, i, n)

    i, j = n-1, n-1
    while i >= 0 and j >= 0:
        if arr[0] < arr2[0]:
            result.append(arr[0])
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, 0, i)
            i-=1
        else:
            result.append(arr2[0])
            arr2[0], arr2[j] = arr2[j], arr2[0]
            heapify(arr2, 0, j)
            j-=1
    if i >=0:
        while i >= 0:
            result.append(arr[0])
            arr[0], arr[i] = arr[i], arr[0]
            heapify(arr, 0, i)
            i-=1
    if j >=0:
        while j >= 0:
            result.append(arr2[0])
            arr2[0], arr2[j] = arr2[j], arr2[0]
            heapify(arr, 0, j)
            j-=1
        
    return result

print(heap(arr,arr2,len(arr)))