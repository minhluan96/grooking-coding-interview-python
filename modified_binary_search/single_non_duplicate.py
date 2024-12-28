def single_non_duplicate(nums): 
    left = 0
    right = len(nums) - 1

    while left != right:
        mid = (left + right) // 2
        if mid % 2 != 0:
            mid = mid - 1
        
        if nums[mid] != nums[mid + 1]:
            right = mid
        else:
            left = mid + 2 # in pairs
    
    return nums[left]

nums = [1,1,2,2,3,3,4,4,5,8,8]
print(single_non_duplicate(nums))