"""
https://leetcode.com/problems/integer-to-english-words
"""

UNDER_20_MAPPING = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
}

OVER_20_MAPPING = {
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety",
}

APPENDAGE = {
    0: "",
    1: "Thousand",
    2: "Million",
    3: "Billion",
    4: "Trillion",
    5: "Quadrillion",
}


def three_to_words(num):
    """
    Take a three digit number and turn it into text.

    ie; 100 -> "One Hundred"
    """

    as_str = str(num)

    if num < 20:
        return UNDER_20_MAPPING[num]

    elif num < 100:
        first_str = OVER_20_MAPPING[int(as_str[0])]
        second_str = UNDER_20_MAPPING[int(as_str[1])]
        return " ".join([first_str, second_str]).strip()

    else:
        first_str = f"{UNDER_20_MAPPING[int(as_str[0])]} Hundred"
        next_str = as_str[1:3]
        next_num = int(next_str)

        if next_num < 20:
            next_str_full = UNDER_20_MAPPING[next_num]

        elif next_num < 100:
            second_str = OVER_20_MAPPING[int(next_str[0])]
            third_str = UNDER_20_MAPPING[int(next_str[1])]
            next_str_full = " ".join([second_str, third_str])

        return " ".join([first_str, next_str_full]).strip()


def determine_chunks(num):
    """
    Break a potentially big number up into chunks of three.
    """

    chunks = {}
    chunk_count = 0
    chunk = []
    num_str = str(num)

    for i, _ in enumerate(num_str):

        letter = num_str[len(num_str) - 1 - i]

        if i % 3 == 0 and i != 0:
            chunk = [letter]
            chunk_count += 1
            chunks[chunk_count] = chunk

        else:
            chunk.insert(0, letter)
            chunks[chunk_count] = chunk

    return chunks


def integer_to_words(num):
    """
    Take an integer and turn it into an English word.
    """
    words = []
    chunks = determine_chunks(num)

    for chunk_num, chunk in chunks.items():
        as_int = int("".join(chunk))
        as_word = three_to_words(as_int)
        appendage = APPENDAGE[chunk_num]
        if as_word != "":
            word_to_insert = " ".join([as_word, appendage])
            words.insert(0, word_to_insert)

    return " ".join(words)
