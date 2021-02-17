# -------------------------------------------------------------
# #	Daily Code	02/17/2021
#   "String to Integer and Vice Versa" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------

# Write two functions:
# to_int(): a function to convert a string to an integer
# to_str(): a function to convert an integer to a string

# Examples:
# to_int("77") -> 77
# to_int("532") -> 532
# to_str(77) -> "77"
# to_str(532) -> "532"

def to_int(txt):
    convertInt = int(txt)
    return convertInt

def to_str(num):
    convertNum = str(num)
    return convertNum

print to_int("77")
print to_int("532")
print to_str(77)
print to_str(532)
