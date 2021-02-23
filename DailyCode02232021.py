# ---------------------------------------------------
# #	Daily Code	02/23/2021
#   "Proper Modulo Operator" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------

# Create a function which returns the Modulo of the two given numbers

# mod(-13, 64) -> 51
# mod(50, 25) -> 0
# mod(-6, 3) -> 0

def mod(x, y):
    solution = x % y
    return solution

print mod(-13, 64)
print mod(50, 25)
print mod(-6, 3)