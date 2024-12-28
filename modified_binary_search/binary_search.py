def binary_search(nums, target):

    left = 0
    right = len(nums) - 1
    mid = float('inf')
    is_found = False

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            is_found = True
            break

        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return mid if is_found else -1

nums = [-2621]
target = -10000
print(binary_search(nums, target))