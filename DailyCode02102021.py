# ------------------------------------------------------
# #	Daily Code	02/10/2021
#   "Basic Variable Assignment" Lesson from edabit.com
#   Coded by: Banehowl
# ------------------------------------------------------

# A student learning Python was trying ot make a function. His code should concatenate a passing string name with
# string "Edabit" and store it in a variable called result. He needs your help to fix this code

# name_string("Mubashir") -> "MusbashirEdabit"
# name_string("Matt") -> "MattEdabit"
# name_string("python") -> "pythonEdabit"

def name_string(name):
    b = "Edabit"
    result = name + b
    return result

print name_string("Mubashir")
print name_string("Matt")
print name_string("python")