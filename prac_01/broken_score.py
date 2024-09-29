"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASS_SCORE = 50
EXCELLENT_SCORE = 90

score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid score")
else:
    if score < PASS_SCORE:
        print("Bad")
    elif score < EXCELLENT_SCORE:
        print("Passable")
    else:
        print("Excellent")






