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


def read_guitars_from_file(file_name):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(file_name, 'r') as in_file:
            reader = csv.reader(in_file)
            for row in reader:
                if row:  # Skip empty lines
                    name, year, cost = row
                    guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with an empty list.")
    return guitars


def write_guitars_to_file(file_name, guitars):
    """Write the list of Guitar objects to a CSV file."""
    with open(file_name, 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Display the list of guitars."""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
