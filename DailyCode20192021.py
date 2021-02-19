# ----------------------------------------------
# #	Daily Code	02/19/2021
#   "Basketball Points" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------

# You are counting points for a basketball game, given the amount of 3-pointers scored and 2-pointers scored,
# find the final points for the team and return that value ([2 -pointers scored, 3-pointers scored]).

# points(1, 1) -> 5
# points(7, 5) -> 29
# points(38, 8) -> 100

def points(twopointers, threepointers):
    twoTotal = twopointers * 2
    threeTotal = threepointers * 3
    total = twoTotal + threeTotal
    return total

print points(1, 1)
print points(7, 5)
print points(38, 8)
