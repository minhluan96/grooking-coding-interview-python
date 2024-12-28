def is_not_cycle(nums, prev_direction, pointer):
    current_direction = nums[pointer] >= 0

    # If current direction and previous direction is different or moving a pointer takes back to the same value,
    # then the cycle is not possible, we return True, otherwise return False.
        
    return (prev_direction != current_direction) or (abs(nums[pointer] % len(nums) == 0))
    
def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    
    return result


def circular_array_loop(nums):  
    size = len(nums)
    
    for i in range(size):
        slow = fast = i

        # Set true in 'forward' if element is positive, set false otherwise.
        foward = nums[i] > 0

        while True:
            # Move slow pointer to one step.
            slow = next_step(slow, nums[slow], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, foward, slow):
                break

            # First move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, foward, fast):
                break

            # Second move of fast pointer.
            fast = next_step(fast, nums[fast], size)
            # If cycle is not possible, break the loop and start from next element.
            if is_not_cycle(nums, foward, fast):
                break

            if slow == fast:
                return True

    return False


arr = [1,3,-2,-4,1]
# arr = [2,1,-1,-2]
print(circular_array_loop(arr))