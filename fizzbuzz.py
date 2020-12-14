"""
Kind of a dumb one...

"""


def fizzBuzz(n):
    nums = []

    for i in range(1, n + 1):
        if i % 5 == 0 and i % 3 == 0:
            val = "FizzBuzz"
        elif i % 5 == 0:
            val = "Buzz"
        elif i % 3 == 0:
            val = "Fizz"
        else:
            val = str(i)

        nums.append(val)

    return nums
