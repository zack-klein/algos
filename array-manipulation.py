"""
https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""


def arrayManipulation(n, queries):

    array = [0 for _ in range(n + 1)]

    for i, query in enumerate(queries):

        # n - 1 problem -> solve by subtracting 1 from a and b
        a = query[0] - 1
        b = query[1]
        k = query[2]

        for j in range(a, b):  # May actually want regular b here

            next_val = array[j] + k
            array[j] = next_val

    max_val = max(array)

    return max_val
