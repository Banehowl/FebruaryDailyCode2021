# --------------------------------------------------------------
#	Daily Code	02/06/2021
#   "Find the Perimeter of a Rectangle" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------------------------

# A vehicle needs 10 times the amount of fuel than the distance it travels. However, it must always carry a minimum
# of 100 fuel before setting off.

# Create a function which calculates the amount of fuel it needs, given the distance.

# calculate_fuel(15) -> 150
# calculate_fuel(23.5) -> 235
# calculate_fuel(3) -> 100

def calculate_fuel(n):
    fuel = n * 10

    if fuel < 100:
        fuel = 100
        return(fuel)
    elif fuel >= 100:
        return(fuel)

print calculate_fuel(15)
print calculate_fuel(23.5)
print calculate_fuel(3)

