"""
https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
"""


def findKthLargest(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return sorted(nums)[-k]
