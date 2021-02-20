# ---------------------------------------------------
# #	Daily Code	02/20/2021
#   "Are the Numbers Equal?" Lesson from edabit.com
#   Coded by: Banehowl
# ---------------------------------------------------
# Create function that returns True when num1 is equal to num2; otherwise return False
# is_same_num(4, 8) -> False
# is_same_num(2, 2) -> True
# is_same_num(2, "2") -> False

def is_same_num(num1, num2):
    if num1 == num2:
        return True
    else:
        return False
print is_same_num(4, 8)
print is_same_num(2, 2)
print is_same_num(2, "2")
