from karel.stanfordkarel import *

"""
File: StepUpKarel.py
--------------------
Our first Karel program, where Karel picks up a beeper,
jumps up on a step and drops the beeper off.
"""


# The program starts by executing a special function called main
def main():
    # Commands are executed one at a time starting here
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_right()    # will execute  turn_right function, then keep executing from here
    move()
    put_beeper()
    move()


# This function has Karel face to the right of whatever
# direction Karel was facing before.
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# This is "boilerplate" code which launches your code
# when you type "python3 StepUpKarel.py" (on Mac) or
# "py StepUpKarel.py" (on PC) in the terminal
if __name__ == "__main__":
    run_karel_program()
