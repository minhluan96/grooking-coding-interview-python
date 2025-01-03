from heapq import *

def binary_search(arr):
    low = 0
    high = len(arr)

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] == 1:
            low = mid + 1
        else:
            high = mid

    return low

def find_k_weakest_rows(matrix, k):
    max_heap = []

    for i, row in enumerate(matrix):
        strength = binary_search(row)
        entry = (-strength, -i)

        if len(max_heap) < k or entry > max_heap[0]:
            heappush(max_heap, entry)
        
        if len(max_heap) > k:
            heappop(max_heap)

    results = []
    while max_heap:
        (_, index) = heappop(max_heap)
        results.append(-index)

    return results[::-1]

matrix = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
k = 2
print(find_k_weakest_rows(matrix, k))
