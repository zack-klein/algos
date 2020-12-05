"""
https://leetcode.com/problems/majority-element/
"""


def majorityElement(nums):
    hash_table = {}
    majority_min = len(nums) / 2

    for num in nums:
        count = hash_table.get(num, 0)
        count += 1
        hash_table[num] = count

    for key, value in hash_table.items():
        if value > majority_min:
            return key
