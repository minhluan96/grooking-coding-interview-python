def jump_game(nums):
    intial_target_index = len(nums) - 1

    for i in range(intial_target_index - 1, -1, -1):
        if intial_target_index <= i + nums[i]:
            intial_target_index = i

    if intial_target_index == 0:
        return True

    return False


nums = [3,2,1,0,4]
results = jump_game(nums)

print(results)