def find_duplicate(nums):
    size = len(nums)
    fast = slow = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast


nums = [1,3,6,2,7,3,5,4]
print(find_duplicate(nums))