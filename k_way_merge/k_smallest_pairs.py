from heapq import *


def k_smallest_pairs(list1, list2, k):

    list_length = len(list1)
    min_heap = []
    pairs = []

    for i in range(min(k, list_length)):
        heappush(min_heap, (list1[i] + list2[0], i, 0))

    counter = 1

    while min_heap and counter <= k:
        sum_of_pairs, i, j = heappop(min_heap)
        pairs.append([list1[i], list2[j]])

        next_element = j + 1

        # if next element is available for list2 then add it to the heap
        if next_element < len(list2):
            heappush(min_heap, (list1[i] + list2[next_element], i, next_element))
        
        counter += 1

    return pairs


list1 = [1,2,300]
list2 = [1,11,20,35,300]
k = 30

print(k_smallest_pairs(list1, list2, k))