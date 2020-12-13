"""
It feels like cheating to use Python's built-in PriorityQueue, but figured
I would practice with it anyway.

Priority queues are implemented using a binary heap (it's commonly
misunderstood that Priority queues and heaps are the same, but they are not!),
which has O(log(n)) lookup and removal times.

Great explanation of how Priority Queues work under the hood:
https://www.youtube.com/watch?v=HCEr35qpawQ&list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu&index=15
"""

import random

from queue import PriorityQueue


def find_nth_largest(nums, n):
    """
    Use a Priority Queue to find the `n` largest element in an array.
    """
    q = PriorityQueue()

    for num in nums:
        # Python does smallest first, so we invert twice! This is #1.
        q.put(num * -1)

    # n determines how many times to pop!
    for i in range(n - 1):
        q.get()

    nth_largest = q.get()
    return nth_largest * -1  # This is inversion #2.


# Tests
# Find the second largest value in an array.
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(arr)
expected_second_largest = 8
actual_second_largest = find_nth_largest(arr, 2)

assert expected_second_largest == actual_second_largest
