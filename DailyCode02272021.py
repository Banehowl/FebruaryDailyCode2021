# -----------------------------------------------------------
# #	Daily Code	02/27/2021
#   "Cocatenating Two Integer Lists" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------------------

# Create a function to concatenate two integer list

# concat([1, 3, 5], [2, 6, 8]) -> [1, 3, 5, 2, 6, 8]
# concat([7, 8], [10, 9, 1, 1, 2]) -> [7, 8, 10, 9, 1, 1, 2]
# concat([4, 5, 1], [3, 3, 3, 3, 3]) -> [4, 5, 1, 3, 3, 3, 3, 3]

def concat(lst1, lst2):
    solution = lst1 + lst2
    return solution

print concat([1, 3, 5], [2, 6, 8])
print concat([7, 8], [10, 9, 1, 1, 2])
print concat([4, 5, 1], [3, 3, 3, 3, 3])