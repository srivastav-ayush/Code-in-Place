from karel.stanfordkarel import *

"""
File: SteepleChaseKarel.py
--------------------------
Karel runs a steeple chase the is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""

"""
To run a race that is 9 avenues long, we need to move
forward or jump hurdles 8 times.
"""
def main():
    for i in range(8):
        if front_is_clear():
            move()
        else:
            jump_hurdle()


"""
Pre-condition:  Facing East at bottom of hurdle
Post-condition: Facing East at bottom in next avenue after hurdle
"""
def jump_hurdle():
    ascend_hurdle()
    move()
    descend_hurdle()

"""
Pre-condition:  Facing East at bottom of hurdle
Post-condition: Facing East immediately above hurdle 
"""
def ascend_hurdle():
    turn_left()
    while right_is_blocked():
        move()
    turn_right()

"""
Pre-condition:  Facing East above and immediately after hurdle
Post-condition: Facing East at bottom of hurdle
"""
def descend_hurdle():
    turn_right()
    move_to_wall()
    turn_left()

"""
Pre-condition:  none
Post-condition: Facing first wall in whichever direction
                Karel was facing previously
"""
def move_to_wall():
    while front_is_clear():
        move()

"""
Pre-condition:  none
Post-condition: Karel is facing to the right of whichever
                direction Karel was facing previously
"""
def turn_right():
    for i in range(3):
        turn_left()



# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
