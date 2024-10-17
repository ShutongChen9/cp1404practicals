import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Check and print quick picks."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_pick = make_quick_pick()
        print_quick_pick(quick_pick)


def make_quick_pick():
    """Make quick pick based on random numbers."""
    quick_pick = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM, MAXIMUM)
        while number in quick_pick:
            number = random.randint(MINIMUM, MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    return quick_pick


def print_quick_pick(quick_pick):
    """Print quick picks."""
    print(" ".join(f"{number:2}" for number in quick_pick))


main()