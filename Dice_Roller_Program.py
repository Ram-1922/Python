#Dice roller program

# print("\u250C \u25CF \u2500 \u2510 \u2502 \u2514 \u2518")
# ┌ ● ─ ┐ │ └ ┘

import random

dice = []
total = 0
num_of_dice = int(input("How many dice: "))
dice_shape = {
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"),
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│      ●  │",
       "└─────────┘"),
    3:("┌─────────┐",
       "│  ●      │",
       "│    ●    │",
       "│      ●  │",
       "└─────────┘"),
    4:("┌─────────┐",
       "│ ●     ● │",
       "│         │",
       "│ ●     ● │",
       "└─────────┘"),
    5:("┌─────────┐",
       "│ ●     ● │",
       "│    ●    │",
       "│ ●     ● │",
       "└─────────┘"),
    6:("┌─────────┐",
       "│ ●  ●  ● │",
       "│         │",
       "│ ●  ●  ● │",
       "└─────────┘")
}

for i in range(num_of_dice):
    dice.append(random.randint(1,6))
    total+=dice[i]

# for die in range(num_of_dice):
#     for i in dice_shape.get(dice[die]):
#         print(i)

for line in range(5):
    for die in dice:
        print(dice_shape.get(die)[line],end="  ")
    print()

print(f"The Total is {total}")