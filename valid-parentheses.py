"""
https://leetcode.com/problems/valid-parentheses/
"""


def isValid(self, s: str) -> bool:
    CLOSINGS = {
        "(": ")",
        "{": "}",
        "[": "]",
    }

    stack = []

    for i, letter in enumerate(s):

        expected_close = CLOSINGS.get(letter)

        if i == 0 and letter not in CLOSINGS:
            return False

        elif len(stack) == 0:
            if letter in CLOSINGS:
                stack.append(CLOSINGS[letter])
            else:
                return False

        elif letter == stack[-1]:
            stack.pop()

        else:
            if letter in CLOSINGS:
                stack.append(expected_close)
            else:
                return False

    if len(stack) != 0:
        return False
    else:
        return True
