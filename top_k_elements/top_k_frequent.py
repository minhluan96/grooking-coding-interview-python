from heapq import heappush, heappop

def top_k_frequent(arr, k):
    min_heap = []
    character_frequencies = {}
    
    for i in range(len(arr)):
        if arr[i] not in character_frequencies:
            character_frequencies[arr[i]] = 0
        character_frequencies[arr[i]] += 1

    for key, val in character_frequencies.items():
        if len(min_heap) <= k:
            heappush(min_heap, (val, key))
        
        if len(min_heap) > k:
            heappop(min_heap)



    return [min_heap[i][1] for i in range(len(min_heap))]

arr = [5,1,-1,-8,-7,8,-5,0,1,10,8,0,-4,3,-1,-1,4,-5,4,-3,0,2,2,2,4,-2,-4,8,-7,-7,2,-8,0,-8,10,8,-8,-2,-9,4,-7,6,6,-1,4,2,8,-3,5,-9,-3,6,-8,-5,5,10,2,-5,-1,-5,1,-3,7,0,8,-2,-3,-1,-5,4,7,-9,0,2,10,4,4,-4,-1,-1,6,-8,-9,-1,9,-9,3,5,1,6,-1,-2,4,2,4,-6,4,4,5,-5] 
k = 7
print(top_k_frequent(arr, k))