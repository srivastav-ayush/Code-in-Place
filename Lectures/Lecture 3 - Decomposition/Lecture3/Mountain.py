from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size
and plants a beeper at the top
"""
def main():
    ascend_mountain()
    put_beeper()
    descend_mountain()

# pre: karel is at the top of a mountain!
# post: karel is on the east side of the mountain
def descend_mountain():
    while front_is_clear():
        step_down()

def step_down():
    move()
    turn_right()
    move()
    turn_left()

# pre: karel is facing a mountain
# post: karel is on the top of said mountain!!!
def ascend_mountain():
    while front_is_blocked():
        step_up()


# pre: karel is facing a step of the mountain
# post: karel is up one step also facing the mountain
def step_up():
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    for i in range(3):
        turn_left()










if __name__ == "__main__":
    run_karel_program()