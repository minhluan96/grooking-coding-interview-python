def backtrack(start_index, subset, total_subset, combination, nums, k):
    if total_subset == k:
        combination.append(subset[::])
        return
    
    for j in range(start_index, len(nums)):
        subset.append(nums[j])
        new_total = total_subset + nums[j]
        backtrack(j + 1, subset, new_total, combination, nums, k)
        subset.pop()

def get_k_sum_subsets(nums, k):
    subset = []
    results = [] 
    start = 0 
    total = 0
    backtrack(start, subset, total, results, nums, k)

    return results

nums = [8,13,3,22,17,39,87,45,36]
k = 3
result = get_k_sum_subsets(nums, k)
print(result)