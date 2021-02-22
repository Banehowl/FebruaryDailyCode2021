# ----------------------------------------------------------------------
# #	Daily Code	02/21/2021
#   "Is the Number Less than or Equal to Zero?" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------------------------------

# Create a function that takes a number as its only argument and returns True if it's less than or equal to zero,
# ortherwise return False

# less_than_or_equal_to_zero(5) -> False
# less_than_or_equal_to_zero(0) -> True
# less_than_or_equal_to_zero(-2) -> True

def less_than_or_equal_to_zero(num):
    if num <= 0:
        return True
    else:
        return False
print less_than_or_equal_to_zero(5)
print less_than_or_equal_to_zero(0)
print less_than_or_equal_to_zero(-2)
