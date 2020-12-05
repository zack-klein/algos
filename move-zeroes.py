"""
https://leetcode.com/problems/move-zeroes/
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    zeroes = []
    proper_order = []

    for num in nums:

        if num == 0:
            zeroes.append(0)

        else:
            proper_order.append(num)

    proper_order += zeroes

    for i, proper_num in enumerate(proper_order):

        nums[i] = proper_num
