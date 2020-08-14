from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should 
solve the "repair the quad" problem from Assignment 1. You
should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    # Karel starts at the position (1,1) facing East.

    # The tasks three things that Karel has to do are:
    # 1. Fix the 1st pillar
    # 2. Move to the next pillar
    # 3. Continue till all pillars are fixed.

    while front_is_clear():
        fix_pillar()
        move_to_next_pillar()
    # Fencepost error correction
    fix_pillar()


# Defining a function for Karel to fix the pillar
def fix_pillar():
    # Fixing the current pillar
    turn_left()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
            move()
    # Code to overcome the fencepost error
    if no_beepers_present():
        put_beeper()


# Defining a function to move Karel to the next position
def move_to_next_pillar():
    # Moving to the bottom of the next pillar
    turn_around()

    while front_is_clear():
        move()

    turn_left()
    move()
    move()
    move()
    move()


# Defining a function to turn Karel right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Defining the function to turn around Karel
def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
