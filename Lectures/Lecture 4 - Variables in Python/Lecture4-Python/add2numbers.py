"""
File: add2numbers.py
--------------------
Another python program to get some practice with variables.
This program asks the user for two integers and prints their sum.
"""

def main():
    print("This program adds two numbers.")
    num1 = input("Enter first number: ")
    num1 = int(num1)
    num2 = input("Enter second number: ")
    num2 = int(num2)
    total = num1 + num2
    print("The total is " + str(total) + ".")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
