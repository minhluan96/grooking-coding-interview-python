def min_sub_array_len(target, nums):

    window_size = float('inf')
    sum = 0
    window_start = 0
    for window_end in range(len(nums)):
        current_num = nums[window_end]

        sum += current_num

        while sum >= target:
            window_size = min(window_size, window_end - window_start + 1)
            num_start = nums[window_start]
            sum -= num_start
            window_start += 1

    
    return window_size if window_size != float('inf') else 0


nums = [1,2,3,4]
target = 10

print(min_sub_array_len(target, nums))