arr = [2,3,4,-5,1]

# Heap sort sorts a list by;
# Heapifying the list which means:
#  creating a binary tree that follows the rules:
#    Min-Heap: Parent <= all children
#    Max-heap: Parent >= all children
#    Note: all levels but the last must be filled (Complete bianry tree)
#  Start from mid-point-1:
#   If the children are >= (or <=) swap and then recursively call the previous values. Rinse and repeat untill the root

# Then Heapsort is called where we echange the value at position 0 (root) and position n-(i+1) last child. We then call Heapsort again now with the start as the root
# Repeat untill i = n
# Time Complexity O(nlog(n))
# Space Complexity O(1)

def heapify(arr, n, i):
     # Initialize largest as root
    largest = i 
    
    #  left index = 2*i + 1
    l = 2 * i + 1 
    
    # right index = 2*i + 2
    r = 2 * i + 2  

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

def heap_sort(arr):
    if len(arr) <= 1:
        return arr
    
    n = len(arr) 

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
      
        # Move root to end
        arr[0], arr[i] = arr[i], arr[0] 

        # Call max heapify on the reduced heap
        heapify(arr, i, 0)
    return arr


print(heap_sort(arr))