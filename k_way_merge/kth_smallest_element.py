from heapq import *

def kth_smallest_element(matrix, k):
    DEFAULT_INDEX = 0
    min_heap = []
    count = 0
    kth_smallest = float('inf')

    for i in range(len(matrix)):
        if matrix[i]:
            heappush(min_heap, (matrix[i][DEFAULT_INDEX], i, DEFAULT_INDEX))

    while min_heap:
        (top_val, list_index, pos_index) = heappop(min_heap)
        kth_smallest = top_val
        if pos_index + 1 < len(matrix[list_index]):
            heappush(min_heap, (matrix[list_index][pos_index + 1], list_index, pos_index + 1))
            
        count += 1
        if count == k:
            break
    
    return kth_smallest if kth_smallest != float('inf') else 0

matrix = [[2,6,8],[3,7,10],[5,8,11]]
k = 3
print(kth_smallest_element(matrix, k))

