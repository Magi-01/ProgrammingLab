arr = [-4,1,2,3,4,5,6,36,40]

# Binary search needs a sorted list; it finds the midpoint
# checks if the value matches:
#   if greater, checks the right side
#   if equal returns the values
#   if less, checks the left side
# rinse anf repeat untill you find the value else "Not found"
# Time Complexity O(log(n))
# Space Complexity O(1)
def binary(arr, n, k):
    left, right = 1, n

    while right > 1:
        mid = (left + right) // 2

        if arr[mid] == k:
            return k
        
        if arr[mid] < k:
            left = mid
        else:
            right = mid
            
    return "Not found"

print(binary(arr, len(arr), 40))