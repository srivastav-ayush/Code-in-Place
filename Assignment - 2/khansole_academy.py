"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

# Mastery count is the number of questions the user has to solve correctly in a row to master addition
MASTERY_COUNT = 3


def main():

    # Setting the number of correct answers to 0 in the starting
    correct = 0

    while correct <= MASTERY_COUNT - 1:

        # Performing the addition of two random two digit numbers
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        add = num1 + num2

        # Asking the addition question to the user, taking input from the user and displaying the answer
        print("What is " + str(num1) + ' + ' + str(num2) + '?')
        ans = int(input("Your answer: "))

        # Printing the result of correct or incorrect answer by the user
        if ans == add:
            correct += 1
            print("Correct! You've gotten " + str(correct) + " correct in a row.")
            continue
        else:
            correct = 0
            print("Incorrect. The expected answer is " + str(add))
            continue

    # Printing congratulations when the user has mastered addition
    if correct == MASTERY_COUNT:
        print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
