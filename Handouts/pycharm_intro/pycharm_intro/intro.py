#!/usr/bin/env python3

"""
CS106A Intro
"""

import sys
import platform


def main():
    if platform.python_version() != "3.8.1":
        print("ERROR: You are not using Python 3.8.1! You are using version: " + platform.python_version())
        print("Please follow the instructions on the CS106A website to download python version 3.8.1")
        return
    if len(sys.argv) != 2:
        print("Hello, CS106A! Now, try running 'python3 intro.py <YOUR NAME HERE>' in the terminal!")
    else:
        name = " ".join(sys.argv[1:])
        print("Hello, " + name + "! You're done with the PyCharm setup process!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
