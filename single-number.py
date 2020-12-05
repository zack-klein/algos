"""
https://leetcode.com/problems/single-number/
"""


# Two passes with a hash table, not great but gets the job done
def singleNumber(nums) -> int:
    ht = {}

    for num in nums:
        current_count = ht.get(num, 0)
        current_count += 1
        ht[num] = current_count

    for num, count in ht.items():
        if count == 1:
            magic_number = num

    return magic_number
