"""
https://leetcode.com/problems/non-decreasing-array/

Needed to look at the solutions for this one.
"""

# Brute force - Slooooow
def checkPossibilityBruteForce(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    def is_ascending(nums):
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                return True

            if num > nums[i + 1]:
                return False

    duplicate_list = nums[:]

    for i, num in enumerate(nums):
        duplicate_list[i] = nums[i - 1] if i > 0 else float('-inf')

        if is_ascending(duplicate_list):
            return True

        duplicate_list[i] = num

    return False
