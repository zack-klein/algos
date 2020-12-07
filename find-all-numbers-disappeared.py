"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


def findDisappearedNumbers(nums):
    s = set(nums)
    expected_nums = []
    missing = []

    for i in range(len(nums)):
        expected_nums.append(i + 1)

    for expected in expected_nums:
        if expected not in s:
            missing.append(expected)

    return missing
