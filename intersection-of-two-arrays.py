"""
https://leetcode.com/problems/intersection-of-two-arrays/
"""


def intersection(nums1, nums2):
    left = set(nums1)
    right = set(nums2)

    intersection = set()

    for num in left:
        if num in right:
            intersection.add(num)

    return list(intersection)
