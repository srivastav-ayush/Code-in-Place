from karel.stanfordkarel import *

"""
File: FillRowKarel.py
---------------------
Karel lays down a whole row of beepers.
BUGGY -- off by one bug
Need to add a final put_beeper()
"""


def main():
    while front_is_clear():
        put_beeper()
        move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
