def can_split(nums, k, mid):
    sub_arrays = 1
    current_sum = 0

    for num in nums:
         # Check if adding the current number exceeds the allowed sum (mid)
        if current_sum + num > mid:
            sub_arrays += 1
            current_sum = num

            if sub_arrays > k:
                return False
        else:
            current_sum += num
    
    return True

def split_array(nums, k):
    max_number = max(nums)
    left = max_number
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2

        # Check if the array can be split into k or fewer subarrays with this maximum sum
        if can_split(nums, k, mid):
            # If possible, try a smaller maximum sum
            right = mid
        else:
            # Otherwise, increase the range to allow larger sums
            left = mid + 1

    # Return the smallest maximum sum that satisfies the condition
    return left

nums = [7,2,5,10,8]
k = 2
print(split_array(nums, k))