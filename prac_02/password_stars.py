MINIMUM_LENGTH = 6


def main():
    """Get password and print stars."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get password and make sure the length of password longer than the minimum length."""
    password = input(f"Enter your password (at least {MINIMUM_LENGTH}): ")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid")
        password = input(f"Enter your password (at least {MINIMUM_LENGTH}): ")
    return password


def print_stars(password):
    """Print stars according to the length of password."""
    print("*" * len(password))


main()