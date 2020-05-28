"""
https://leetcode.com/problems/basic-calculator-ii/
"""

import re


# Times out... but works!
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    equation = re.split("(\D)", s.replace(" ", ""))  # noqa:W605 $$$

    if len(equation) == 1:
        return int(equation[0])

    if len(equation) == 3 and equation[0] == "":
        return int(s)

    if equation[0] == "":
        del equation[0]
        neg_val = f"-{equation[1]}"
        del equation[0]
        del equation[0]
        equation.insert(0, neg_val)

    for i, element in enumerate(equation):  # $$$

        # If there is multiplication or division
        if element == "*" or element == "/":

            operator = element
            left = int(equation[i - 1])
            right = int(equation[i + 1])

            if operator == "*":
                result = left * right

            if operator == "/":
                result = left / right

            del equation[i + 1]
            del equation[i]
            del equation[i - 1]
            equation.insert(i - 1, str(result))  # $$$
            return calculate(
                "".join(equation)
            )  # Call again with one less multi/div

    # After that ^^ loop, we are guaranteed to have a non multi/div operation
    operator = equation[1]
    left = int(equation[0])
    right = int(equation[2])

    if operator == "+":
        result = left + right

    else:
        result = left - right

    del equation[2]
    del equation[1]
    del equation[0]

    equation.insert(0, str(result))  # $$$
    return calculate("".join(equation))
