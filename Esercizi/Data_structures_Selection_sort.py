arr = [2,3,4,-5,1]

# Selection sort sorts a list by;
# checking if the value at the n-(i+1)-th place is the largest:
#   if true, takes the values position
# iterates this way untill the i-th values and then swaps the positions
# Time Complexity O(n^2)
# Space Complexity O(1)
def selection(arr, n):
    right = n-1
    while right > 0:
        left = right
        max = right
        while left >= 0:
            if arr[left] > arr[max]:
                max = left
            left -= 1
        arr[right], arr[max] = arr[max], arr[right]
        right -= 1
    return arr

print(selection(arr, len(arr)))