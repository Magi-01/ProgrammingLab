arr = [2,3,4,-5,1]

# Insertion sort sorts a list by;
# checking if the value at the i-th position is the larger than (i-1)-th position:
#   if true, swaps the positions
# iterates this way n-2 times
# Time Complexity O(n^2)
# Space Complexity O(1)
# Note: Works best on partially sorted arrays 
#   O(k*n) where k is the distance from being sorted
#   for each element (e.g. [5,6,7,1,2,3] has k = 3)
def insertion(arr, n):
    right = 0
    while right < n-1:
        left = right
        while left >= 0:
            if arr[left] > arr[left+1]:
                arr[left], arr[left+1] = arr[left+1], arr[left]
            else:
                left = 0
            left -= 1
        right += 1
    return arr

print(insertion(arr, len(arr)))