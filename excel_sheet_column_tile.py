"""
https://leetcode.com/problems/excel-sheet-column-title/

Couldn't solve it, used this solution:
https://leetcode.com/problems/excel-sheet-column-title/discuss/641281/Python-Using-string-lib
"""
import string


def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    letters = list(string.ascii_uppercase)
    result = ""
    while n != 0:
        n, r = divmod(n - 1, 26)
        result = letters[r] + result
    return result
