total_price = 0
DISCOUNT_STANDARD = 100
DISCOUNT_RATE = 0.1
MINIMUM_ITEMS = 0

number_of_items = int(input("Number of items: "))
while number_of_items < MINIMUM_ITEMS:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item

if total_price > DISCOUNT_STANDARD:
    total_price *= (1 - DISCOUNT_RATE)
print(f"Total price for {number_of_items} items is ${total_price:.2f}")