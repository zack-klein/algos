"""
https://leetcode.com/problems/move-zeroes/
"""


# Uses two arrays, concatenates, then reconstructs
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


# Uses two pointers
def moveZeroesTwoPointers(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    first_zero = None

    for i, num in enumerate(nums):
        if num == 0:
            first_zero = i
            break

    if first_zero is not None:

        slow = first_zero
        current = first_zero + 1

        while current < len(nums):

            if nums[current] != 0:
                nums[slow] = nums[current]
                nums[current] = 0

                slow += 1

            current += 1

    return nums
