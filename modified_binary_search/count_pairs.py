def count_pairs(nums, target):
  
    sorted_nums = sorted(nums)
    count = 0

    for i in range(len(sorted_nums)):
        low = i + 1
        high = len(sorted_nums)

        while low < high:
            mid = low + (high - low) // 2

            if sorted_nums[i] + sorted_nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        # Add the count of valid pairs for this iteration
        count += low - (i + 1)

    return count
# [1,2,3,4,5]
nums = [1,3,2,4,5]
target = 6
print(count_pairs(nums, target))