# --------------------------------------------
# #	Daily Code	02/14/2021
#   "Football Points" Lesson from edabit.com
#   Coded by: Banehowl
# --------------------------------------------

# Create a function that takes the nubmer of wins, draws, and losses and calculates the number of points a football
# team has obrtained so far
# wins ges 3 points
# draws get 1 point
# losses get 0 points

# football_points(3, 4, 2) -> 13
# football_points(5, 0, 2) -> 15
# football_points(0, 0, 1) -> 0

def football_points(wins, draws, losses):
    winTotal = wins * 3
    drawTotal = draws * 1
    lossTotal = losses * 0
    totalPoints = winTotal + drawTotal + lossTotal
    return(totalPoints)

print football_points(3, 4, 2)
print football_points(5, 0, 2)
print football_points(0, 0, 1)