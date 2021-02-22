# -----------------------------------------------
# #	Daily Code	02/22/2021
#   "Fix the Expression" Lesson from edabit.com
#   Coded by: Banehowl
# -----------------------------------------------

# Fix the code in the Code tab so the function returns true if and only if x is equal to 7. Try to debug code and pass
# all the tests.

# is_seven(4) -> False
# is_seven(9) -> False
# is_seven(7) -> True

# def is_seven(x):
# 	return False if x=7 elif True

def is_seven(x):
    if x == 7:
        return True
    else:
        return False

print is_seven(4)
print is_seven(9)
print is_seven(7)
