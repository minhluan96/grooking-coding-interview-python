def calculate_sum(index, mid, n):
    count = 0

    # calculate the left side of the index
    if mid > index:
        # if mid is greater than the index, then the arithmetic sequence is 
        # [mid - index, mid - index + 1, mid - 1, ..., mid]
        count += (mid + mid - index) * (index + 1) // 2
    else:
        # otherwise, the arithmetic sequence is [1,2,3,...mid - 1, mid]
        # in addition, there will be (mid - index + 1) numbers of 1s
        count += (mid + 1) * mid // 2 + index - mid + 1
    
    # calculate the right side of the index
    if mid >= n - index:
        # if mid is greater than or equal to n - index, the arithmetic series is
        # [mid, mid - 1, mid - 2, ... , mid - n + 1 + index]
        count += (mid + mid - n + 1 + index) * (n - index) // 2
    else:
        # otherwise, the arithmetic sequence is [mid, mid-1, mid-2, ...,3,2,1]
        # in addition, there will be (n - index - mid) number of 1s
        count += (mid + 1) * mid // 2 + n - index - mid

    # subtract the mid at the index because it counted twice
    return count - mid


def max_value(n, index, max_sum):
    left = 1
    right = max_sum

    while left < right:
        mid = (left + right + 1) // 2
        # move to the right half if its valid
        if calculate_sum(index, mid, n) <= max_sum:
            left = mid
        else:
            right = mid - 1

    # the maximum valid mid at the index
    return left

n = 8
index = 5
max_sum = 25
print(max_value(n, index, max_sum))
