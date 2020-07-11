"""
https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/
"""


# Brute force solution. The worst case time complexity occurs when you have an
# array of strings that are all already sorted (because the algorithm needs
# to traverse each letter of each string). This makes it O(n^m), where `n` is
# the number of words in the array and `m` is the number of letters in each
# word.
# The space complexity is linear -- each solution will only ever need to store
# the hash table, the value of the current word, the next word, and the `i`th
# element of the current and next words. This makes the space complexity
# O(n + (n*2) + (m*2)) (might be a cleaner way to write that <-), where `n` is
# the memory consumed a word and `m` is the memory consumed by a letter.
# This does surprisingly well, as it is faster than 70% of solutions.
def isAlienSorted(words, order):
    """
    :type words: List[str]
    :type order: str
    :rtype: bool
    """

    # First we build the hash table
    orders = {}

    for i, letter in enumerate(order):
        orders[letter] = i

    # Next, we walk the `words` array and compare for sorting
    for current_word_i, current_word in enumerate(words):

        # Only evaluate the next word if it exists
        if current_word_i < len(words) - 1:

            next_word = words[current_word_i + 1]

            for current_word_letter_i, current_word_letter in enumerate(
                current_word
            ):

                # If this index doesn't exist in the next letter, they can't
                # be sorted, because if they were sorted it would have been
                # caught already
                if current_word_letter_i > len(next_word) - 1:
                    return False

                # Only evaluate the next letter if it has a letter at this
                # index
                else:
                    next_word_letter = next_word[current_word_letter_i]

                    current_word_letter_order = orders[current_word_letter]
                    next_word_letter_order = orders[next_word_letter]

                    # Not sorted!
                    if current_word_letter_order > next_word_letter_order:
                        return False
                    # Sorted!
                    elif current_word_letter_order < next_word_letter_order:
                        break

                    # Same letter
                    else:
                        pass

    return True
