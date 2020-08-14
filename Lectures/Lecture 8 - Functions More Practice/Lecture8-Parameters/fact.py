"""
File: fact.py
-------------
This program prints out the factorials of numbers up to MAX_NUM
"""

MAX_NUM = 4


def factorial(n):
    """
    This function returns the factorial of n (denoted n!)
    Input: n (number to compute the factorial of)
    Returns: value of n factorial
    Doctests:
    >>> factorial(3)
    6
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    """
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result



def main():
    """
    Prints factorials for all numbers from 0 to MAX_NUM
    """
    for i in range(MAX_NUM):
        print(i, factorial(i))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
