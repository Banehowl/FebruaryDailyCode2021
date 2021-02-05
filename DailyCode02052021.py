# --------------------------------------------------------------
#	Daily Code	02/05/2021
#   "Find the Perimeter of a Rectangle" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

# Create a function that takes length and width and finds the perimeter of a rectangle
# find_perimeter(6, 7) -> 26
# find_perimeter(20, 10) -> 60
# find_perimeter(2, 9) -> 22

def find_perimeter(length, width):
    solution = (2 * length) + (2 * width)
    return(solution)

print find_perimeter(6, 7)
print find_perimeter(20, 10)
print find_perimeter(2, 9)