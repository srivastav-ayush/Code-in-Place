"""
File: rolldice.py
------------------
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

import random

# Number of sides on each die to roll
NUM_SIDES = 6

def main():
    # setting seed is useful for debugging
    # random.seed(1)
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Dice have " + str(NUM_SIDES) + " sides each.")
    print("First die: " + str(die1))
    print("Second die: " + str(die2))
    print("Total of two dice: " + str(total))

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()