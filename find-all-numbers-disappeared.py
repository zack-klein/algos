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


def findDisappearedNumbersConstantSpace(nums):

    for i, num in enumerate(nums):
        proper_index = abs(num) - 1
        value_at_index = nums[proper_index]

        if value_at_index > 0:
            nums[proper_index] = value_at_index * -1

    missing = []
    for i, num in enumerate(nums):

        if num > 0:
            missing.append(i + 1)

    return missing
