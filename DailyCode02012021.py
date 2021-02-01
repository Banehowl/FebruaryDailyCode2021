# -------------------------------------------------------
#	Daily Code	02/01/2021
#   "Convert Hours into Seconds" Lesson from edabit.com
#   Coded by: Banehowl
# -------------------------------------------------------

# Write a fuction that converts hours into seconds
# how_many_seconds(2) -> 7200
# how_many_seconds(10) -> 36000
# how_many_seconds(24) -> 86400

def how_many_seconds(hours):
    seconds = hours * 3600
    return(seconds)

print how_many_seconds(2)
print how_many_seconds(10)
print how_many_seconds(24)
