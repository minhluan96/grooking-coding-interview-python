from utils.traversal import *

def merge_sorted(nums1, m, nums2, n):

    p1 = m - 1
    p2 = n - 1

    for p in range(m + n - 1, -1, -1):
        if p2 < 0:
            break

        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1

    return nums1

nums1 = [6,7,8,9,10,0,0,0,0,0]
nums2 = [1,2,3,4,5]
m = 5
n = 5

result = merge_sorted(nums1, m, nums2, n)
print(result)