"""
https://leetcode.com/problems/house-robber/
"""


# This is wizardry, need to revisit this and come to the conclusion myself
def rob(self, nums):
    current = 0
    prev = 0

    for i, num in enumerate(nums):
        temp = current
        current = max(prev + num, current)
        prev = temp

    return current
