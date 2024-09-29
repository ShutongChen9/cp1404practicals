import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASS_SCORE = 50
EXCELLENT_SCORE = 90


def main():
    """Get score and print the score level."""
    score = float(input("Enter score: "))
    print(determine_level(score))

    # Add a new part to the bottom of your main function that generates a random score and prints the result.
    score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(score, determine_level(score))


def determine_level(score):
    """Determine the score level."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score < PASS_SCORE:
        return "Bad"
    elif score < EXCELLENT_SCORE:
        return "Passable"
    else:
        return "Excellent"


main()