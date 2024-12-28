from heapq import *

class MedianOfStream:

    def __init__(self):
        self.max_h = []
        self.min_h = []
        heapify(self.min_h)
        heapify(self.max_h)

    # This function should take a number and store it
    def insert_num(self, num):
        if not self.max_h or -self.max_h[0] >= num:
            heappush(self.max_h, -num)
        else:
            heappush(self.min_h, num)

        self.rebalance()

        
    # This function should return the median of the stored numbers
    def find_median(self):
        if len(self.max_h) == len(self.min_h):
            return -self.max_h[0] / 2 + self.min_h[0] / 2

        return -self.max_h[0]           
        
    def rebalance(self):
        if len(self.max_h) > len(self.min_h) + 1:
            top_el = -heappop(self.max_h)
            heappush(self.min_h, top_el)
        elif len(self.max_h) < len(self.min_h):
            top_el = heappop(self.min_h)
            heappush(self.max_h, -top_el)

["MedianOfStream","insert_num","find_median","insert_num","find_median","insert_num","find_median","insert_num","find_median","insert_num","find_median"] 
[[],[-1],[],[-22],[],[-3],[],[-4],[],[-5],[]]

mos = MedianOfStream()
mos.insert_num(-1)
print(mos.find_median())
mos.insert_num(-22)
print(mos.find_median())
mos.insert_num(-3)
print(mos.find_median())
mos.insert_num(-4)
print(mos.find_median())
mos.insert_num(-5)
print(mos.find_median())

