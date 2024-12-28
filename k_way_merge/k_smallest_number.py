from heapq import *


def k_smallest_number(lists, k):
    if not lists:
        return 0
    
    min_heap = []
    has_pop_map = {}
    DEFAULT_INDEX = 0
    count = 0
    k_element = -1

    for index, list in enumerate(lists):
        if list:
            heappush(min_heap, (list[DEFAULT_INDEX], index))
        has_pop_map[index] = DEFAULT_INDEX


    while min_heap:
        (smallest, list_index) = heappop(min_heap)
        current_pos = has_pop_map[list_index]
        selected_list = lists[list_index]

        if current_pos < len(selected_list) - 1:
            heappush(min_heap, (selected_list[current_pos + 1], list_index))
            has_pop_map[list_index] = current_pos + 1

        count += 1
        k_element = smallest
        
        if count == k: 
            break

    
    return k_element if k_element != -1 else 0

lists = [[1,2,3],[4,5],[6,7,8,15],[10,11,12,13],[5,10]]
k = 50
print(k_smallest_number(lists, k))