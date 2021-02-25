# ---------------------------------------------------------------
# #	Daily Code	02/25/2021
#   "Find the Smallest Number in a List" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------------------

# Create a function that takes a list of numbers and returns the smallest number in the list.

# find_smallest_num([34, 15, 88, 2]) -> 2
# find_smallest_num([34, -345, -1, 100]) -> -345
# find_smallest_num([-76, 1.345, 1, 0]) -> -76
# find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999]) -> -0.9999
# find_smallest_num([7, 7, 7]) -> 7

def find_smallest_num(nums):
    lowestNum = min(nums)
    return lowestNum

print find_smallest_num([34, 15, 88, 2])
print find_smallest_num([34, -345, -1, 100])
print find_smallest_num([-76, 1.345, 1, 0])
print find_smallest_num([0.4356, 0.8795, 0.5435, -0.9999])
print find_smallest_num([7, 7, 7])