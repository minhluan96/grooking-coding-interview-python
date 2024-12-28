def find_max_sliding_window(nums, w):
    output = []

    for i in range(len(nums)):
        window_end = i + w if i + w < len(nums) else len(nums)
        window_start = i

        max_val = nums[window_start]
        if len(nums[window_start:window_end]) < w:
            continue

        while window_start < window_end:
            max_val = max(nums[window_start], max_val)
            window_start += 1
        
        output.append(max_val)

    return output

##################

from collections import deque

def clean_up(i, current_window, nums):
    # remove all the indexes from current_window whose corresponding values are smaller than or equal to the current element
    while current_window and nums[i] >= nums[current_window[-1]]:
         current_window.pop()


    

def alternative_solution(nums, w):
    if len(nums) == 1:
        return nums
    
    output = []
    current_window = deque()

    for i in range(w):
        clean_up(i, current_window, nums)
        current_window.append(i)

    # appending the maximum element of the current window to the output list
    output.append(nums[current_window[0]])

    for i in range(w, len(nums)):
        # for every element, remove the previous smaller elements from current_window
        clean_up(i, current_window, nums)

        # remove first index from the current_window if it has fallen out of the current window
        if current_window and current_window <= (i - w):
            current_window.popleft()

        current_window.append(i)

        # appending the maximum element of the current window to the output list
        output.append(nums[current_window[0]])
    
    return output


arr = [1,2,3,4,5,6,7,8,9,10]
w = 3
print(find_max_sliding_window(arr, w))
print(alternative_solution(arr, w))