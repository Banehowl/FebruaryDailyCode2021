# --------------------------------------------------------------
# #	Daily Code	02/24/2021
#   "Find the Largest Number in a List" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

# Create a function that takes a list of numbers. Return th elargest number in the list.

# findLargestNum([])
# findLargestNum([4, 5, 1, 3]) -> 5
# findLargestNum([300, 200, 600, 150]) -> 600
# findLargestNum([1000, 1001, 857, 1]) -> 1001

def findLargestNum(nums):
    largeNum = max(nums)
    return largeNum

print findLargestNum([4, 5, 1, 3])
print findLargestNum([300, 200, 600, 150])
print findLargestNum([1000, 1001, 857, 1])