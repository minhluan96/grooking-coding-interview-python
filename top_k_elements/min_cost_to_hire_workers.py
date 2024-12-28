from heapq import *

class Solution:
    
    def __init__(self):
        self.max_heap = []

    
    def min_cost_to_hire_workers(self, quality, wage, k):
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heappush(self.max_heap, -q)
            total_quality += q

            if len(self.max_heap) > k:
                # remove top el since it is the max heap, the top val is negative value
                total_quality += heappop(self.max_heap)
            
            if len(self.max_heap) == k:
                min_cost = min(min_cost, ratio * total_quality)

        return min_cost
    

quality = [4, 5, 6]
wage = [8, 10, 12]
k = 2

solution = Solution()
print(solution.min_cost_to_hire_workers(quality, wage, k))