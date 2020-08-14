"""
File: calculateage.py
------------------
This program runs carbon dating (how cool!)
The ratio of normal carbon (carbon-12) to carbon-14 in the air
and in all living things at any given time is nearly constant.
Maybe one in a trillion carbon atoms are carbon-14. Carbon-12 is
stable, but Carbon-14 decays with a half-life of approximately
5,730 years. After the organism dies it stops taking in new carbon.
"""
import math

HALF_LIFE = 5730
HALF_LIFE_CONSTANT = HALF_LIFE / math.log(0.5)


def main():
    print("Carbon dating")
    calculate_age_single_sample()


def calculate_age_single_sample():
    # use the half life formula to calculate the age
    # https://en.wikipedia.org/wiki/Radiocarbon_dating
    pct_left = float(input("% of natural c14 in your sample: "))
    age = math.log(pct_left / 100) * HALF_LIFE_CONSTANT
    print("Your sample is " + str(age) + " years old.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()