"""
https://leetcode.com/problems/rotate-array/submissions/
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    rotation = 0

    while rotation < k:

        last = nums.pop()
        nums.insert(0, last)

        rotation += 1
