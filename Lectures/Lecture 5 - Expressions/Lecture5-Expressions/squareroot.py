"""
File: squareroot.py
-------------------
This program asks the user for a number and
prints its square root.
"""

import math

def main():
    num = float(input("Enter number: "))
    root = math.sqrt(num)
    print("Square root of " + str(num) + " is " + str(root))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
