from karel.stanfordkarel import * 

"""
File: RhoombaKarel.py
----------------------------
Pick up all the beepers in the world.
"""

def main():
    while left_is_clear():
        # Pre: Karel is facing East, start of row
        clear_row()
        next_row()
        # Post: Karel is facing East, start of next row
    clear_row()


# pre: karel is at the start of a messy row
# post: karel is at the end of a clean row
def clear_row():
    while front_is_clear():
        safe_pick()
        move()
    safe_pick()


# pick up, but only if there is a beeper
def safe_pick():
    if beepers_present():
        pick_beeper()


# pre: karel is at the end of a clean row
# post: karel is at the start of the next messy row
def next_row():
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()


def move_to_wall():
    while front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
