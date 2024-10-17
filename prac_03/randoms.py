import random

print(random.randint(5, 20))  # line 1
# Smallest number: 5  Largest number: 20

print(random.randrange(3, 10, 2))  # line 2
# Smallest number: 3  Largest number: 9
# Cannot produce a 4, because the step is 2, only can produce 3, 5, 7, 9

print(random.uniform(2.5, 5.5))  # line 3
# Smallest number: 2.5  Largest number: 5.5


# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
