"""
https://leetcode.com/problems/subarray-sum-equals-k/
"""


# Get every possible subarray. n**3 time complexity.
def subarraySumBruteForce(self, nums, k):
    counter = 0

    # Loop through the array once
    for i, num in enumerate(nums):

        # Loop through every possible subarray
        for j in range(i, len(nums) + 1):

            current_sum = sum(nums[i:j])

            if current_sum == k and nums[i:j] != []:
                counter += 1

    return counter


# This is wizardry...
# https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
def subarraySum(self, nums, k):
    count = 0
    sums = 0
    d = dict()
    d[0] = 1

    for i in range(len(nums)):
        sums += nums[i]
        count += d.get(sums - k, 0)
        d[sums] = d.get(sums, 0) + 1

    return count
