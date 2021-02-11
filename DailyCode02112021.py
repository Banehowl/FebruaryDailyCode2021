# -------------------------------------------------
# #	Daily Code	02/11/2021
#   "To the Power of ____" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------

# Create a function that takes a base number and an exponent number and returns the calculation
# calculate_exponent(5, 5) -> 3125
# calculate_exponent(10, 10) -> 1000000000
# calculate_exponent(3, 3) -> 27

def calculate_exponent(num, exp):
    solution = num ** exp
    return(solution)

print calculate_exponent(5, 5)
print calculate_exponent(10, 10)
print calculate_exponent(3, 3)

