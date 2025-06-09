arr = [1,2,4,-1,3,5,6,7,8]

def fun(arr):
    n = len(arr)
    lindex = 0
    rindex = 0
    length = 0
    curr_start = 0
    curr_length = 1
    for i in range(1,n):
        if arr[i] > arr[i-1]:
            curr_length+=1
        else:
            if curr_length > length:
                length = curr_length
                lindex = curr_start
                rindex = i
            curr_length = 1
            curr_start = i
    if curr_length > length:
        lindex = curr_start
        rindex = n-1
    return arr[lindex:rindex]

print(fun(arr))