def get_bit(num, bit):
    # shifts the first operand the specified number of bits to the left
    temp = (1 << bit)
    # if a specific bit in the binary number is set, then return 1 else return 0
    temp = temp & num

    if temp == 0:
        return False
    
    return True

def find_all_subsets(nums):
    length = len(nums)
    total_subsets = pow(2, length)

    results = []

    for i in range(total_subsets):
        # Set is created to store each subset
        subset = set()
        for j in range(0, len(nums)):
            if get_bit(i, j) == 1 and nums[j] not in subset:
                subset.add(nums[j])

        # for first iteration subset list will always have an empty list
        if i == 0:
            results.append([])
        else:
            results.append(list(subset))

    return results

nums = [2,5,7]
print(find_all_subsets(nums))