"""
https://leetcode.com/problems/valid-palindrome-ii/
"""


# Times out, but works!
def validPalindrom(s):
    # Is is already a palindrome?
    if s == s[::-1]:
        return True
    else:

        letters = [l for l in s]

        for i, letter in enumerate(letters):
            without_s_list = letters[:i] + letters[i + 1 :]  # noqa: E203

            without_s = "".join(without_s_list)
            if without_s == without_s[::-1]:
                return True
    return False


# Linear time complexity (only one array), constant memory complexity (only
# pointers are stored in memory.)
def validPalindromePointers(s: str) -> bool:
    """
    We can use two pointers, one from the start and from the end, to compare
    mismatches in the two arrays.
    """
    p1 = 0
    p2 = len(s) - 1

    for i, _ in enumerate(s):

        if s[p1] != s[p2]:
            without_p1 = s[:p1] + s[p1 + 1 :]  # noqa: E203

            if without_p1 == without_p1[::-1]:
                return True

            without_p2 = s[:p2] + s[p2 + 1 :]  # noqa: E203

            if without_p2 == without_p2[::-1]:
                return True

            return False

        p1 += 1
        p2 -= 1

    return True
