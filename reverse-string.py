"""
https://leetcode.com/problems/reverse-string/
"""


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    half = len(s) // 2

    for i in range(half):
        temp = s[i]
        opposite = s[len(s) - 1 - i]
        s[i] = opposite
        s[len(s) - 1 - i] = temp
