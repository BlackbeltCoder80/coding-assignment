# Import Random





import random

while True:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1}, Dice 2: {dice2}.")
    if dice1 == dice2:
        print(f"Both dice landed on {dice1}.")
        break