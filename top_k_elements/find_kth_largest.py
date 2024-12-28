from heapq import *

def find_kth_largest(nums, k):
    min_heap = []

    for i in range(k):
        heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        root = min_heap[0]
        if nums[i] > root:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return min_heap[0]

nums = [5,2,9,-3,7]
k = 5
print(find_kth_largest(nums, k))