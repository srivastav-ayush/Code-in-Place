"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    # This is a program that takes two numbers as input and reports their subtraction as the output
    print("This program subtracts one number from another.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    subtraction = num1 - num2
    print("The result is " + str(subtraction))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
