"""
https://leetcode.com/problems/third-maximum-number/
"""


# The Python cheater's answer:
def thirdMaxBruteForce(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    distinct = sorted(set(nums))

    if len(distinct) < 3:
        return max(distinct)

    return distinct[-3]
