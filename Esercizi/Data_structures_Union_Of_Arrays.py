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
        heapify(arr, n, largest)


def heap(arr,arr2,n):
    result = []

    for i in range(n - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0]
        arr2[0], arr2[i] = arr2[i], arr2[0]

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
        heapify(arr2, i, 0)
    return result

print(heap(arr,arr2,len(arr)))