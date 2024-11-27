from random import choice, randint, shuffle

# fruit = choice(["apple", "banana", "cherry"])
# print(f"I'd like a {fruit} please!")

# # Random number between 1 and 10
# number = randint(1, 10)
# print(f"Random number: {number}")

cards = ["jack", "queen", "king", "ace"]
shuffle(cards)
for card in cards:
    print(card)