"""
https://leetcode.com/problems/longest-common-prefix/
"""


# Brute Force
def longestCommonPrefixBruteForce(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    prefix = ""
    final_prefix = ""
    first_word = next(iter(strs), [])

    for letter in first_word:
        prefix += letter

        for i, word in enumerate(strs):

            if word.startswith(prefix) and i == (len(strs) - 1):
                final_prefix = prefix
            elif word.startswith(prefix):
                pass
            else:
                return final_prefix

    return final_prefix


# Optimized - Divide and Conquer
def get_prefix(str1, str2):
    """
    Get the longest common prefix between 2 strings.

    :type str1: str
    :type str2: str
    """
    prefix = ""
    final_prefix = ""

    for letter in str1:
        prefix += letter

        if str2.startswith(prefix):
            final_prefix = prefix

        else:
            return final_prefix
    return final_prefix


def longestCommonPrefixOptimized(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if strs == []:
        return ""
    if len(strs) == 1:
        return strs[0]
    elif len(strs) == 2:
        prefix = get_prefix(strs[0], strs[1])
        return longestCommonPrefixOptimized([prefix])
    else:
        middle = len(strs) // 2
        left = longestCommonPrefixOptimized(strs[middle:])
        right = longestCommonPrefixOptimized(strs[:middle])
        return longestCommonPrefixOptimized([left, right])
