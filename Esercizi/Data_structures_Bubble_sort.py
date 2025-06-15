arr = [2,3,4,-5,1]

# Bubble sort sorts a list by;
# checking if the value at the i-th position is the larger than (i-1)-th position:
#   if true, swaps the positions
# iterates this way untill the n-(i+1)-th position
# Time Complexity O(n^2)
# Space Complexity O(1)
def bubble(arr, n):
    right = n-1
    while right >= 0:
        left = 0
        while left < right:
            if arr[left] > arr[left+1]:
                arr[left], arr[left+1] = arr[left+1], arr[left]
            left += 1
        right -= 1
    return arr

print(bubble(arr, len(arr)))