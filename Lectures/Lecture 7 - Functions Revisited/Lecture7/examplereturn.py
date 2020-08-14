"""
File: examplefor.py
------------------
Print the first 100 even numbers
"""
import math

METERS_PER_FEET = 0.3
INCH_PER_FEET = 12

def main():
    while True:
        num_feet = int(input('num feet? '))
        num_inches = int(input('num inches? '))
        num_meters = convert_feet_and_inches_to_meters(num_feet, num_inches)
        print('num meters', num_meters)


def convert_feet_and_inches_to_meters(num_feet, num_inches):
    print('converting...')

    # this calculates num meters just using the "feet" not the "inches"
    num_meters_in_feet_part = METERS_PER_FEET * num_feet

    # this calculates num meters just using the "inches"
    num_meters_in_inch_part = (num_inches / INCH_PER_FEET) * METERS_PER_FEET

    # add them up for your final answer
    return num_meters_in_feet_part + num_meters_in_inch_part


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()