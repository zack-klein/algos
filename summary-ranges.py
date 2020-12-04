"""
https://leetcode.com/problems/summary-ranges/submissions/
"""


# Haaaaack and a half but works well
def summaryRanges(nums):
    ranges = []

    # Edge cases
    if len(nums) == 0:
        return []

    if len(nums) == 1:
        return [str(nums[0])]

    if len(nums) == 2:
        if nums[1] != nums[0] + 1:
            return [str(nums[0]), str(nums[1])]
        else:
            return [f"{nums[0]}->{nums[1]}"]

    for i, num in enumerate(nums):

        if i == 0:
            base = num
            end = num

        elif i == len(nums) - 1:
            if num != end + 1:
                if base != end:
                    ranges.append(f"{base}->{end}")
                else:
                    ranges.append(str(base))

                ranges.append(str(num))
            else:
                ranges.append(f"{base}->{num}")

        else:
            if num != end + 1:

                if base == end:
                    ranges.append(str(base))
                else:
                    ranges.append(f"{base}->{end}")

                base = num
                end = num

            else:
                end = num
    return ranges
