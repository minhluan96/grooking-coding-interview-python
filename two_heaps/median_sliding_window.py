from heapq import *

def median_sliding_window(nums, k):
    medians = []
    outgoing_nums = {}

    # max heap
    small_list = []

    # min heap
    large_list = []

    # variable to calculate the balance
    balance = 0

    for i in range(k):
        heappush(small_list, -nums[i])

    # transfer 50% of small list to large list
    for i in range(k // 2):
        el = heappop(small_list)
        heappush(large_list, -el)

    i = k
    while True:
        # if the window size is odd
        if k % 2 != 0:
            medians.append(float(-small_list[0]))
        else:
            medians.append((float(-small_list[0]) + float(large_list[0])) * 0.5)

        if i >= len(nums):
            break

        # calculate outgoing number to hashmap to track it for removing later
        out_num = nums[i - k]

        in_num = nums[i]
        i += 1

        # if out num is on top of the max heap
        if out_num <= -small_list[0]:
            balance -= 1
        else:
            balance += 1

        # add / update out num to the hashmap
        if out_num in outgoing_nums:
            outgoing_nums[out_num] = outgoing_nums[out_num] + 1
        else:
            outgoing_nums[out_num] = 1

        

        # if the incoming num is less than top of the max heap, add it to the max heap, otherwise add to the min heap
        if small_list and in_num <= -small_list[0]:
            balance += 1
            heappush(small_list, -in_num)
        else:
            balance -= 1
            heappush(large_list, in_num)

        # rebalance the heap
        if balance < 0:
            heappush(small_list, -large_list[0])
            heappop(large_list)
        elif balance > 0:
            heappush(large_list, -small_list[0])
            heappop(small_list)

        # since the heap has been rebalanced, we reset balance back to 0
        # This ensures that the two heaps contain the correct elements for the calculations to be performed on the elements in the next window.
        balance = 0

        # remove invalid numbers present in hashmap from top of max heap
        while (-small_list[0] in outgoing_nums and outgoing_nums[-small_list[0]] > 0):
            outgoing_nums[-small_list[0]] -= 1
            heappop(small_list)
        
        # remove invalid numbers present in hashmap from top of min heap
        while (large_list and large_list[0] in outgoing_nums and outgoing_nums[large_list[0]] > 0):
            outgoing_nums[large_list[0]] -= 1
            heappop(large_list)

    return medians


nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(median_sliding_window(nums, k))