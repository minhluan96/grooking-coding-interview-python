from heapq import *

def max_subsequence(nums, k):
    min_heap = []

    for i in range(len(nums)):
        if len(min_heap) < k:
            heappush(min_heap, (nums[i], i))
        else:
            (top_el, _) = min_heap[0]
            if nums[i] > top_el:
                heappop(min_heap)
                heappush(min_heap, (nums[i], i))
    
    min_heap.sort(key=lambda item: item[1])
    result = [key for key, _ in min_heap]
    return result

nums = [2,1,4,4]
k = 2
print(max_subsequence(nums, k))