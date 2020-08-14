"""
File: dicesimulator.py
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

import random

# Number of sides on each die to roll
NUM_SIDES = 6

# Simulates rolling two dice and prints their total
def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Total of two dice: " + str(total))


def main():
    random.seed(1)
    die1 = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is: " + str(die1))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()