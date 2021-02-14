# -------------------------------------------------------------------
# #	Daily Code	02/13/2021
#   "Return the First Element from the List" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------------

# Create a function that takes a list containing only numbers and return the first element
# get_first_value([1, 2, 3]) -> 1
# get_first_value([80, 5, 100]) -> 80
# get_first_value([500, 0, 50]) -> 500

def get_first_value(number_list):
    first_list = number_list[0]
    return(first_list)

print get_first_value([1, 2, 3])
print get_first_value([80, 5, 100])
print get_first_value([500, 0, 50])