"""
File: buggytrace.py
-------------------
This program is an example to help you trace through code.
The "bug" is that parameters of primitive types (such as int)
are passed by value, so changes to a parameter in a function
don't change the variable outside the function.
"""

# NOTE: This program is buggy!!

def add_five(x):
    x += 5


def main():
    x = 3
    add_five(x)
    print("x = " + str(x))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
