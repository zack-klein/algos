"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


# Brute Force - Fails time limit
def twoSumBruteForce(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, num in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            complement = target - num
            if numbers[j] == complement:
                return [i + 1, j + 1]


# Brute Force 2 - Still fails time limit
def twoSumBruteForce2(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i, num in enumerate(numbers):
        for j in range(i + 1, len(numbers)):
            complement = target - num
            if numbers[j] == complement:
                return [i + 1, j + 1]
            elif numbers[j] > complement:
                break


# Optimized - 2 pass hash table - This does well
def twoSumHashTable(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Use the first walk to populate the hash table
    hash_table = {}
    for i, num in enumerate(numbers):
        hash_table[num] = i

    # Use the second walk to check for membership of
    for i, num in enumerate(numbers):
        complement = target - num

        if complement in hash_table:
            return [i + 1, hash_table[complement] + 1]


# Optimized 2 - 1 pass hash table - Faster than 99% of solutions
def twoSumHashTable2(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    hash_table = {}
    for i, num in enumerate(numbers):
        complement = target - num

        if complement in hash_table:
            return [hash_table[complement] + 1, i + 1]

        else:
            hash_table[num] = i
