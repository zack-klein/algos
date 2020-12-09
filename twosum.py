"""
https://leetcode.com/problems/two-sum/submissions/
"""


# Brute Force
def twoSumBruteForce(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - num:
                return [i, j]


# Two iterations hash table
def twoSumTwoIterations(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_table = {}
    for i, num in enumerate(nums):
        hash_table[num] = i

    for i, num in enumerate(nums):
        complement = target - num
        j = hash_table.get(complement)
        if j and j != i:
            return [i, j]


# Single iteration hash table
def twoSumOneIteration(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_table = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_table:
            return [hash_table[complement], i]
        else:
            hash_table[num] = i


# Just revisiting... one of my favorite problems!
def twoSum(self, nums, target):
    ht = {}

    for i, num in enumerate(nums):
        complement = target - num
        complement_index = ht.get(complement)

        if complement_index is not None:
            return (complement_index, i)
        else:
            ht[num] = i
