# ---------------------------------------------
# #	Daily Code	02/15/2021
#   "The Farm Problem" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer
# breeds three species:
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs

# The farmer has counted his animals and he gives you a subttotal for each species. You have to implement a function
# that returns the total number of legs of all the animals.

# Examples:
# animals(2, 3, 5) -> 36
# animals(1, 2, 3) -> 22
# animals(5, 2, 8) -> 50

def animals(chickens, cows, pigs):
    chickenLegs = chickens * 2
    cowLegs = cows * 4
    pigLegs = pigs * 4
    legTotal = chickenLegs + cowLegs + pigLegs
    return(legTotal)

print animals(2, 3, 5)
print animals(1, 2, 3)
print animals(5, 2, 8)