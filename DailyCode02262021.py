# ----------------------------------------------------------------------
# #	Daily Code	02/26/2021
#   "Difference of Max and Min Numbers in List" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------------------------------

# Create a function that takes a list and returns the difference between the biggest and smallest numbers.

# difference_max_min([10, 4, 1, 4, -10, -50, 32, 21]) -> 82
# Smallest number is -50, biggest is 32.

# difference_max_min([44, 32, 86, 19]) -> 67
# Smallest number is 19, biggest is 86.

def difference_max_min(nums):
    maxNum = max(nums)
    minNum = min(nums)
    diffSolution = maxNum - minNum
    return diffSolution

print difference_max_min([10, 4, 1, 4, -10, -50, 32, 21])
print difference_max_min([44, 32, 86, 19])
