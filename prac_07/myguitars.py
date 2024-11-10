"""
My guitars program
Estimate: 55 minutes
Actual:   58 minutes
"""

import csv
from prac_07.guitar import Guitar


def main():
    """Main function to execute the program."""
    file_name = 'guitars.csv'
    guitars = read_guitars_from_file(file_name)
    print("Current guitars:")
    display_guitars(guitars)
    guitars.sort()
    print("\nSorted guitars (by year):")
    display_guitars(guitars)

    while True:
        name = input("\nEnter the name of the guitar (or 'done' to stop): ")
        if name.lower() == 'done':
            break
        year = int(input("Enter the year of the guitar: "))
        cost = float(input("Enter the cost of the guitar: "))
        guitars.append(Guitar(name, year, cost))

    write_guitars_to_file(file_name, guitars)

    print("\nUpdated list of guitars saved to file.")
    print("\nUpdated guitars:")
    display_guitars(guitars)



if __name__ == "__main__":
    main()
