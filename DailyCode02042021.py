# ------------------------------------------------
#	Daily Code	02/04/2021
#   "Convert Age to Days" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------

# Create a function that takes the age and return the age in days
# calc_age(65) -> 23725
# calc_age(0) -> 0
# calc_age(20) -> 7300

def calc_age(age):
    days = age * 365
    return(days)

print calc_age(65)
print calc_age(0)
print calc_age(20)
