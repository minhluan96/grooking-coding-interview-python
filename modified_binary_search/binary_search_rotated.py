def binary_search_rotated(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] == target:
            return mid
        
        # low to mid is sorted
        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                # target is within the sorted first half of the array
                high = mid - 1
            else:
                # target is not within the sorted first half, so let's examine the unsorted second half
                low = mid + 1
        else:
            if nums[mid] < target and target <= nums[high]:
                # target is within the sorted second half
                low = mid + 1
            else:
                # target is not within the second half, so let's examine the unsorted first half
                high = mid - 1

    return -1


###################################
# RECURSIVE APPROACH #
###################################

def binary_search(nums, low, high, target):

    if (low > high):
        return -1

    # Finding the mid using integer division
    mid = low + (high - low) // 2

    if nums[mid] == target:
        return mid

    # low to mid is sorted
    if nums[low] <= nums[mid]:
        if nums[low] <= target and target < nums[mid]:
            # target is within the sorted first half of the array
            return binary_search(nums, low, mid-1, target)
        # target is not within the sorted first half, so let’s examine the unsorted second half
        return binary_search(nums, mid+1, high, target)
    # mid to high is sorted
    else:
        if nums[mid] < target and target <= nums[high]:
            # target is within the sorted second half of the array
            return binary_search(nums, mid+1, high, target)
        # target is not within the sorted second half, so let’s examine the unsorted first half
        return binary_search(nums, low, mid-1, target)


def binary_search_rotated(nums, target):
    return binary_search(nums, 0, len(nums)-1, target)

nums = [6,7,1,2,3,4,5]
target = 6
print(binary_search_rotated(nums, target))