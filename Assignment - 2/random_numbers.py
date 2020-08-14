"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

# Constant to represent the number of random numbers to be printed
NUM_RANDOM = 10
# Constant to represent the minimum value of the random numbers
MIN_RANDOM = 0
# Constant to represent the maximum value of the random numbers
MAX_RANDOM = 100


def main():
    # This program prints a list of random numbers according to the constant values of NUM_RANDOM, MIN_RANDOM,
    # MAX_RANDOM
    for i in range(NUM_RANDOM):
        num = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(num + 1)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
