from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    # Karel has to find the midpoint in its world. If the world is 1 corner or two corners big we have defined it as
    # a special case and the loop ends when faced with such condition with Karel at the midpoint with a beeper. For
    # other cases having a world with 3 or more corners we have constructed a loop of commands to first find the
    # midpoint using the beeper and then removing the excess beepers while returning to the midpoint position.

    # Karel first puts a beeper at the starting position
    put_beeper()
    if front_is_clear():  # Checks if the world is more than one corner, and if it is move one corner
        move()
        if front_is_clear():  # Checks if the world is more than two corners
            find_mid()
            remove_excess_beepers()
            move_to_mid()
        else:  # If Karel is two corners then turn around and place a beeper
            turn_around()
            move_to_mid()


def find_mid():
    place_beeper_wall()
    while no_beepers_present():
        is_it_mid()
        find_beeper()


def remove_excess_beepers():
    pick_beeper_up_along()
    turn_around()
    move_to_mid()
    pick_beeper_up_along()
    turn_around()


def pick_beeper_up_along():
    while front_is_clear():
        move()
        pick_beeper()


def move_to_mid():
    while no_beepers_present():
        move()


# Karel puts a beeper at the wall in front of it and turn around to move one corner
def place_beeper_wall():
    while front_is_clear():
        move()
    put_beeper()
    spin_and_move()


# Karel checks if the current corner is the midpoint
def is_it_mid():
    move()
    if beepers_present():
        spin_and_move()
        put_beeper()


# Karel moves to find the next beeper
def find_beeper():
    if no_beepers_present():
        while no_beepers_present():
            move()
        spin_and_move()
        put_beeper()
        move()


# Makes Karel to turn around and move one corner
def spin_and_move():
    turn_around()
    move()


# Makes Karel to turn around by turning left twice
def turn_around():
    turn_left()
    turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
