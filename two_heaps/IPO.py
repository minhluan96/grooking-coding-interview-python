from heapq import *



def maximum_capital(c, k, capitals, profits):
    current_capital = c
    capitals_min_heap = []
    profits_max_heap = []

    for i in range(len(capitals)):
        heappush(capitals_min_heap, (capitals[i], i))

    TOP_POS = 0
    KEY_POS = 0
    for _ in range(k):
        while capitals_min_heap and capitals_min_heap[TOP_POS][KEY_POS] <= current_capital:
            c, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, profits[i] * -1)

        if not profits_max_heap:
            break

        current_capital += heappop(profits_max_heap) * -1

    return current_capital


c = 1
k = 3
capitals = [0,1,2]
profits = [1,2,3]
result = maximum_capital(c, k, capitals, profits)
print(result)