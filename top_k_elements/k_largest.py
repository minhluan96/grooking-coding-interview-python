from heapq import *

class KthLargest:
    # Constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.min_heap = []
        self.k = k
        for i in range(len(nums)):
            self.add(nums[i])

    # Adds element in the heap and return the Kth largest
    def add(self, val):

        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
        else:
            if self.min_heap and self.min_heap[0] < val:
                heappop(self.min_heap)
                heappush(self.min_heap, val)

        return self.min_heap[0]
    

# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
k = 3
nums = [4,5,8,2]
kth_largest = KthLargest(k, nums)
kth_largest.add(3)
kth_largest.add(5)
kth_largest.add(10)
kth_largest.add(9)
result = kth_largest.add(4)
print(result)
