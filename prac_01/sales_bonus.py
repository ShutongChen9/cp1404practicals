"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

LOW_RATE = 0.1
HIGH_RATE = 0.15
MINIMUM_SALE = 0
MAXIMUM_SALE = 1000


sales = float(input("Enter sales: $"))
while sales >= MINIMUM_SALE:
    if sales < MAXIMUM_SALE:
        bonus = LOW_RATE
    else:
        bonus = HIGH_RATE
    print(f"Bonus: ${int(sales * bonus)}")
    sales = float(input("Enter sales: $"))

