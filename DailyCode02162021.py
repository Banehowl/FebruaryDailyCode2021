# -------------------------------------------------------------------
# #	Daily Code	02/16/2021
#   "Convert Hours and Minutes into Seconds" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------------------

# Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them

# convert(1, 3) -> 3780
# convert(2, 0) -> 7200
# convert(0, 0) -> 0

def convert(hours, minutes):
    conHours = hours * 3600
    conMins = minutes * 60
    conTotal = conHours + conMins
    return(conTotal)

print convert(1, 3)
print convert(2, 0)
print convert(0, 0)
