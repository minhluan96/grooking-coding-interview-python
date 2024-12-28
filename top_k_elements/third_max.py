from heapq import *

def third_max(nums): 
    min_heap = []
    distinct_nums = list(set(nums))

    if len(nums) < 3 or len(distinct_nums) < 3:
        return max(nums)

    for i in range(3):
        heappush(min_heap, distinct_nums[i])

    for i in range(3, len(distinct_nums)):
        if len(min_heap) < 3:
            heappush(min_heap, distinct_nums[i])
        else:
            if min_heap[0] < distinct_nums[i]:
                heappop(min_heap)
                heappush(min_heap, distinct_nums[i])
    
    return min_heap[0] if len(min_heap) >= 3 else max(min_heap)

nums = [2,2,3,1]
print(third_max(nums))