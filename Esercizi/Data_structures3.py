# Given A[1,...,n] of int (positive and negative) 
# find the copy of which sum is 0


def find_null_sum(arr,n):
    if n < 2:
        return 0
    
    if n == 2:
        return int(arr[0] == arr[1])

    count = 0
    seen = set()

    for num in arr:
        if -num in seen:
            count += 1
        seen[num] = 1

    return count

arr = [1,2,-2,3,-1,4]
print(find_null_sum(arr, len(arr)))