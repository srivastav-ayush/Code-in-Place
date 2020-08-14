"""
File: examplefor.py
------------------
Print the first 100 even numbers
"""
import math

MAX_SPACES = 50

def main():
    print_io(0,0)

    # simple forward and back
    for j in range(5):
        for i in range(MAX_SPACES):
            print_io(i,0)
        for i in range(MAX_SPACES, -1, -1):
            print_io(i, 0)

    # split with i staying still
    for i in range(MAX_SPACES):
        print_io(0, i)
    for i in range(MAX_SPACES, -1, -1):
        print_io(0, i)

    # move to the middle
    half_way = MAX_SPACES//2
    for i in range(half_way):
        print_io(i, 0)
    print_diamond(half_way)
    print_diamond(half_way)
    print_diamond(half_way)

def print_diamond(size):
    # split to the edges
    for i in range(size):
        print_io(size - i, i * 2)
    # come back together
    for i in range(size, -1, -1):
        print_io(size - i, i * 2)

def print_io(space_1, space_2):
    print_spaces(space_1)
    print_no_newline('i')
    print_spaces(space_2)
    print_no_newline('o')
    print('')

def print_spaces(n):
    for i in range(n):
        print_no_newline(' ')

def print_no_newline(to_print):
    print(to_print, end="")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()