from heapq import *

def largest_integer(num):
    arr_num = [int(i) for i in str(num)]
    result = []

    max_heap_odd = []
    max_heap_even = []

    for n in arr_num:
        if n % 2 == 0:
            heappush(max_heap_even, -n)
        else:
            heappush(max_heap_odd, -n)

    for n in arr_num:
        if not max_heap_odd or not max_heap_even:
            break
        max_even = -max_heap_even[0]    
        max_odd = -max_heap_odd[0]

        if n % 2 == 0:
            result.append(max_even)
            heappop(max_heap_even)
        else:
            result.append(max_odd)
            heappop(max_heap_odd)

    while max_heap_odd:
        remain = -heappop(max_heap_odd)
        result.append(remain)

    while max_heap_even:
        remain = -heappop(max_heap_even)
        result.append(remain)


    result_num  = ''.join(map(str, result))
    return int(result_num)


num = 589416321

# expected 985634121
print(largest_integer(num))