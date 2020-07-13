"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""


# Slow, but space efficient (94%)!
def minRemoveToMakeValidLists(s):
    """
    :type s: str
    :rtype: str
    """
    opened = []
    to_delete = []

    for i, letter in enumerate(s):

        if letter == "(":
            opened.append(i)

        if letter == ")":
            if len(opened) != 0:
                del opened[-1]
            else:
                to_delete.append(i)

    if len(opened) != 0:
        to_delete += opened

    new_str = ""

    for i, letter in enumerate(s):

        if i not in to_delete:
            new_str += letter

    return new_str
