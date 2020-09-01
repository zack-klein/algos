"""
"""


# Brute force - this times out
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    windows = {}

    for i, letter in enumerate(s):

        start = i
        end = i + len(p)

        if end >= len(s) + 1:
            break

        window = s[start:end]
        windows[i] = window

    indexes = []

    for index, substr in windows.items():

        if sorted(substr) == sorted(p):
            indexes.append(index)

    return indexes


# A O(n) solution that times out! What the heck!
def findAnagrams2(self, s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    indexes = []

    for i, letter in enumerate(s):

        start = i
        end = i + len(p)

        if end >= len(s) + 1:
            break

        window = s[start:end]

        if sorted(window) == sorted(p):
            indexes.append(i)

    return indexes
