import timeit
"""
def combinationSum(candidates, target): 
        results = []
        def rec(i, current, remaining):
          # base cases
          if remaining == 0:
              results.append(current[:])
              return
          if remaining < 0 or i == len(candidates):
              return

          # TAKE candidates[i]
          rec(i, current + [candidates[i]], remaining - candidates[i])

          # LEAVE candidates[i]
          rec(i + 1, current, remaining)

        rec(0, [], target)
        return results


nums = [3,6,7,2]
k = 7
print(combinationSum(nums, k))
print(timeit.timeit("combinationSum(nums, k)", number=10,globals=globals()))
"""
###################
"""
Queue -> FIFO
Stack -> LIFO

Max heap:
    - left child is always smaller than the root and right child is always bigger than the root
    For the i-th node:
        - the root is at floor((i-1)/2)-th position
        - the left child at 2*i-th position
        - the right child at the 2*i + 1 position
Heapify(Max):
    n = heap.size
    L = left(i)
    R = right(i)
    largest = i
    if L<n and heap.L>heap.largest:
        largest = L
    if R<n and heap.R>heap.largest:
        largest = R
    if largest!=i:
        swap(heap, largest, i)
        heapify(heap, largest) 
Given that this step eliminates 1/3 of heap, then we have that T(n) <= T((2/3)*n) + \theta(1) thus T(n) = O(log(n))
Another way to look at it is that each step goes down one level in the binary tree with the max height of h = log(n) and as such T(n) = O(h)
NOTE: We always start the build heap at n/2 given all leaves live in between n/2 and n. This process takes O(n)
NOTE: for heapsort, we build the heap then for i starting at n-1 to 1, you swap the i-th position with the 0-th, pop the last value, then heapify.
The loop takes O(n) while the heapify (starting from 0) takes O(log(n)) thus we have O(nlog(n))
"""
def heapify(A, i):
    n = len(A)
    L = 2*i
    R = 2*i + 1
    largest = i

    if L < n and A[L] > A[largest]:
        largest = L
    if R < n and A[R] > A[largest]:
        largest = R
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        heapify(A, largest)
def buildMaxHeap(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        heapify(A, i)

def Heapsort(A):
    n = len(A)
    tmp =[]
    buildMaxHeap(A)
    for i in range(n-1,-1,-1):
        A[i], A[0] = A[0], A[i]
        tmp.append(A.pop())
        heapify(A,0)
    return tmp


#print(timeit.timeit("Heapsort([3,6,7,2])", number=10000,globals=globals()),Heapsort([3,6,7,2]))

"""
Given an array A of n elements, find the largest subset that is ordered increasingly.

[1,2,3,4,-1,7,6,10,11]

two pointers i,j both starting at 0 and a counter and max counter
while i is >= j move j by one and increment counter
if the updated counter is greater than the current max counter then update the maxcounter and the with i = j - counter return i and maxcounter as indexes
"""

def maxsubset(A):
    n = len(A)
    i,j,counter,maxcounter = 0,1,1,1
    start = 0
    end = 0
    while j<n:
        if A[j] >= A[j-1]:
            counter += 1
        else:
            if counter > maxcounter:
                maxcounter = counter
                end = j - 1
                start = i
                counter = 1
            i = j
            counter = 1
        j += 1
    if counter > maxcounter:
        start = i
        end = n - 1
    return A[start:end+1]
#print(maxsubset([-1,7,10,11,1,2,3,4,6]))

"""
Given an A array of size n find if two value sums to a given value
sort array
Start two pointers one a the end one at the beggining
if the sum is less then move left, if more move right, if left and right intersect, return none
"""

def sumtoValue(A,k):
    A.sort()
    n = len(A)
    l = 0
    r = n - 1
    while l<r:
        if A[l] + A[r] < k:
            l += 1
        elif A[l] + A[r] > k:
            r -= 1
        else:
            return [A[l], A[r]]
    
    return []

#print(sumtoValue([-1,7,10,11,1,2,3,4,6], 10))

"""
Given k arrays ordered, all of lenth n write an algorithim to unite them in O(nlog(k)). USE min heap
"""
import heapq

def HeapSort(A):
    n = len(A[0])
    k = len(A)
    risult = []

    item = [(A[i][0],i,0) for i in range(k)]

    heapq.heapify(item)
    
    while item:
        ele, arr_idx, ele_indx = heapq.heappop(item)
        risult.append(ele)
        if ele_indx + 1 < n:
            heapq.heappush(item, (A[arr_idx][ele_indx + 1], arr_idx, ele_indx + 1))

    return risult

lis = [[-1,7,10], [11,1,2], [3,4,6]]
for l in lis:
    l.sort()

#print(HeapSort(lis))

"""
Given an array>=0 of size n, impement Radix sort
"""

lis = [170, 45, 75, 90, 802, 24, 2, 66]
from collections import defaultdict
max_val = max(lis)
d = len(str(max_val))

def countingSort(g, exp):
    dic = defaultdict(list)
    result = []

    for num in g:
        digit = (num // exp) % 10
        dic[digit].append(num)

    # Rebuild array in digit order
    result = []
    for digit in range(10):   # 0 to 9
        result.extend(dic[digit])

    return result

def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        arr = countingSort(arr, exp)
        exp *= 10

    return arr

print(radix_sort(lis))