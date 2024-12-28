from heapq import *

def find_right_interval(intervals):
    min_heap_start = []
    min_heap_end = []

    result = [-1 for _ in range(len(intervals))]

    # Populate the start_heap and end_heap with intervals (start and end points along with their indices).
    for index, interval in enumerate(intervals):
        [start, end] = interval
        heappush(min_heap_start, (start, index))
        heappush(min_heap_end, (end, index))

    while min_heap_end:
        # Get the interval with the smallest end point.
        (smallest_end, end_index) = heappop(min_heap_end)

        # Remove all start points from start_heap that are smaller than the current end point.
        while min_heap_start and min_heap_start[0][0] < smallest_end:
            heappop(min_heap_start)

        # If start_heap is not empty, the top element is the smallest valid right interval.
        if min_heap_start:
            (_, start_index) = min_heap_start[0]
            result[end_index] = start_index
        
    return result

intervals = [[1,3],[4,6],[7,9],[10,12]]
print(find_right_interval(intervals))