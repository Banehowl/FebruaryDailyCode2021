# ---------------------------------------------------
# #	Daily Code	02/09/2021
#   "Find Out the Leap Year" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------

# Write a function that determines if the year is a leap year or not
# leap_year(2020) -> True
# leap_year(2021) -> False
# leap_year(1968) -> True

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return(True)
        return(False)
    elif year % 400:
        return(True)
    else:
        return(False)

print leap_year(2020)
print leap_year(2021)
print leap_year(1968)