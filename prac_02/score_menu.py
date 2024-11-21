MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
PASS_SCORE = 50
EXCELLENT_SCORE = 90
MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Get choice according to the menu and print the result."""
    score = get_valid_score(MINIMUM_SCORE, MAXIMUM_SCORE)
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(MINIMUM_SCORE, MAXIMUM_SCORE)
        elif choice == "P":
            print(determine_level(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Farewell")


def get_valid_score(low, high):
    """Get valid score."""
    score = int(input("Enter score: "))
    while score < low or score > high:
        print("Invalid")
        score = int(input("Enter score: "))
    return score


def determine_level(score):
    """Determine score level."""
    if score < PASS_SCORE:
        return "Bad"
    elif score < EXCELLENT_SCORE:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    """Print stars according to the score."""
    print("*" * score)


main()

