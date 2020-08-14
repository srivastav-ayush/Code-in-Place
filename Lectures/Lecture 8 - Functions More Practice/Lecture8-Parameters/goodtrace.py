"""
File: goodtrace.py
------------------
This program is an example to help you trace through code.
To modify values of parameters of primitive types (such as int)
we need to return a new value from the function and assign it
to the original variable that is passed into the function.
"""

# NOTE: This program is feeling just fine...

def add_five(x):
    x += 5
    return x


def main():
    x = 3
    x = add_five(x)
    print("x = " + str(x))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
