from karel.stanfordkarel import *

def main():
    move()
    double_beepers_in_pile()
    move_backward()

# For every beeper on the current corner, Karel places
# two beepers on the corner immediately ahead of him.
def double_beepers_in_pile() :
    while beepers_present() :
        pick_beeper()
        put_two_beepers_next_door()
    
    move_pile_next_door_back()

# Place two beepers on corner one avenue ahead of Karel
# and move back to starting position/orientation
def put_two_beepers_next_door() :
    move()
    put_beeper()
    put_beeper()
    move_backward()


# Move all the beepers on the corner in front of Karel
# the the corner Karel is currently on.
def move_pile_next_door_back() :
    move()
    while beepers_present() :
        move_one_beeper_back()
    
    move_backward()


# Move one beeper from the current corner back one avenue
# and return to the original position/orientation.
def move_one_beeper_back() :
    pick_beeper()
    move_backward()
    put_beeper()
    move()


# Move Karel back one avenue, but have the same 
# final orientation.
def move_backward() :
    turn_around()
    move()
    turn_around()

# still a classic.
def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()