"""
https://leetcode.com/problems/majority-element/
"""


# Two pass hash table
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


# One pass hash table
def majorityElementOnePass(nums):
    hash_table = {}
    majority_min = len(nums) / 2

    for num in nums:
        count = hash_table.get(num, 0)
        count += 1

        if count > majority_min:
            return num

        hash_table[num] = count
