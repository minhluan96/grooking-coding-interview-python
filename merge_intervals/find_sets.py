import heapq

def find_sets(intervals):

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    first_interval = sorted_intervals[0]
    
    min_heap = []
    min_heap.append(first_interval[1])

    heapq.heapify(min_heap)

    for i in range(1, len(sorted_intervals)):
        current_interval = sorted_intervals[i]
        [start_curr, end_curr] = current_interval

        if min_heap[0] <= start_curr:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, end_curr)
        else:
            heapq.heappush(min_heap, end_curr)

    return len(min_heap)

intervals = [[2,8],[3,4],[3,9],[5,11],[8,20],[11,15]]
print(find_sets(intervals))
