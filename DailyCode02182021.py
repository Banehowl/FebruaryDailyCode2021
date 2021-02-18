# ----------------------------------------------------
# #	Daily Code	02/18/2021
#   "Return Something to Me!" Lesson from edabit.com
#   Coded by: Banehowl
# ----------------------------------------------------

# Write a function that returns the string "something" joined with a space " " and the given argument a

# give_me_something("is better than nothing") -> "something is better than nothing"
# give_me_something("Bob Jane") -> "something Bob Jane"
# give_me_something("something") -> "Soemthing something"

def give_me_something(a):
    fullString = "something " + a
    return fullString

print give_me_something("is better than nothing")
print give_me_something("Bob Jane")
print give_me_something("something")