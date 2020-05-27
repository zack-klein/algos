"""
https://leetcode.com/problems/find-peak-element/
"""


def evaluate_peak(i, nums):

    if i == 0 or i == (len(nums) - 1):
        return i

    elif nums[i] < nums[i - 1]:
        return evaluate_peak(i - 1, nums)

    elif nums[i] < nums[i + 1]:
        return evaluate_peak(i + 1, nums)

    else:
        return i


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        midpoint = (len(nums) - 1) // 2
        return evaluate_peak(midpoint, nums)
