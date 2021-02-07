# ---------------------------------------------
# #	Daily Code	02/07/2021
#   "Power Calculator" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------

# Create a function that takes voltage and curret and returns the calculated power
# circuit_power(230, 10) -> 2300
# circuit_power(110, 3) -> 330
# circuit_power(480, 20) -> 9600

def circuit_power(voltage, current):
    power = voltage * current
    return(power)

print circuit_power(230, 10)
print circuit_power(110, 3)
print circuit_power(480, 20)