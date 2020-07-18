"""
https://leetcode.com/problems/merge-sorted-array/
"""


# This is the Python cheater's way...
def mergeBruteForce(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = sorted(nums1[:m] + nums2)
    return None


# Using the "two pointer" method...
def merge(self, nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1 = 0
    p2 = 0
    counter = 0
    merged = [0 for _ in range(m + n)]

    nums1[:] = nums1[:m]

    while counter < m + n:

        if p1 > len(nums1) - 1:  # If we've hit the end of 1, add 2
            merged[counter] = nums2[p2]
            p2 += 1
            counter += 1

        elif p2 > len(nums2) - 1:  # If we've hit the end of 2, add rest of 1
            merged[counter] = nums1[p1]
            p1 += 1
            counter += 1

        elif nums1[p1] < nums2[p2] or nums1[p1] == nums2[p2]:
            merged[counter] = nums1[p1]
            p1 += 1
            counter += 1

        elif nums2[p2] < nums1[p1]:
            merged[counter] = nums2[p2]
            p2 += 1
            counter += 1

    nums1[:] = merged
