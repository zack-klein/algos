def is_unique(s):
    seen = []

    for i, letter in enumerate(s):

        if letter in seen:
            return False
        else:
            seen.append(letter)

    return seen


def lengthOfLongestSubstring(self, s: str) -> int:

    if s == " " or len(s) == 1:
        return 1
    # Sliding window!

    L = 0
    R = 1
    max_substr = 0

    while R <= len(s):

        sub_array = s[L:R]

        if is_unique(sub_array):
            R += 1

            if len(sub_array) > max_substr:
                max_substr = len(sub_array)

        elif R > L + 1:
            L += 1

        else:
            R += 1

    return max_substr
