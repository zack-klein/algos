"""
https://leetcode.com/problems/product-of-array-except-self/solution/
"""


# This times out, but technically works!
def productExceptSelfBruteForce(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    products = []

    for i, num in enumerate(nums):

        # First we get the indices we want to multiply for this i
        indices = [_i for _i, _ in enumerate(nums) if _i != i]
        product = 1

        # Then we loop through the indices to get the value and append it
        for index in indices:
            product = product * nums[index]

        products.append(product)

    return products


# This was pretty hard, had to look at the solution.
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Declare Left and Right arrays
    L = []
    R = []

    # Build the L array
    for i, num in enumerate(nums):

        # Deal with the first number
        if i == 0:
            L.append(1)

        else:
            L.append(L[i - 1] * nums[i - 1])

    # Build the R array
    nums.reverse()
    for j, num in enumerate(nums):
        if j == 0:
            R.append(1)

        else:
            R.append(R[j - 1] * nums[j - 1])

    R.reverse()

    # Get the products and append them to the final products
    products = []
    for i, num in enumerate(nums):

        product = L[i] * R[i]
        products.append(product)

    return products
