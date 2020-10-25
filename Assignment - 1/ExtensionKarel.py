from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""


def main():
    # This is a Karel program that prints my name "AYUSH" letter by letter onto the world in RED colour.
    # The program first prints a letter and then erases the letter to print the next letter

    # Karel paints the whole world WHITE
    white_world()
    # Karel paints the letter A on the world
    paint_a()
    origin()
    clear_world()
    # Karel paints the letter Y on the world
    paint_y()
    origin()
    clear_world()
    # Karel paints the letter U on the world
    paint_u()
    origin()
    clear_world()
    # Karel paints the letter S on the world
    paint_s()
    origin()
    clear_world()
    # Karel paints the letter H on the world
    paint_h()
    origin()
    clear_world()


# Karel paints the letter A in the world
# Pre-condition: Karel starts at origin (1,1) facing East
# Post-condition: Karel reaches any position facing East
def paint_a():
    move_to_start()  # Karel reaches the starting point
    turn_left()
    for i in range(10):  # Karel paints the vertical line of A going northwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_right()
    for i in range(7):  # Karel paints the horizontal line of A going eastwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_right()
    for i in range(10):  # Karel paints the vertical line of A going southwards
        put_beeper()
        paint_corner(RED)
        move()
    put_beeper()
    paint_corner(RED)
    turn_around()
    for i in range(5):  # Karel moves to the position to paint the small horizontal line
        move()
    turn_left()
    for i in range(6):  # Karel paints the small horizontal line
        move()
        put_beeper()
        paint_corner(RED)
    move()
    turn_around()


# Karel paints the letter Y in the world
# Pre-condition: Karel starts at origin (1,1) facing East
# Post-condition: Karel reaches any position facing East
def paint_y():
    move_to_start()  # Karel reaches the starting point (7,5) facing East
    for i in range(7):
        move()
    turn_left()
    for i in range(10):  # Karel paints the vertical line of Y going northwards
        put_beeper()
        paint_corner(RED)
        move()
    put_beeper()
    paint_corner(RED)
    turn_around()
    for i in range(5):
        move()
    turn_right()
    for i in range(7):  # Karel paints the horizontal line of Y going eastwards
        move()
        put_beeper()
        paint_corner(RED)
    turn_right()
    for i in range(5):  # Karel paints the small vertical line of Y going northwards
        move()
        put_beeper()
        paint_corner(RED)
    turn_right()


# Karel paints the letter U in the world
# Pre-condition: Karel starts at origin (1,1) facing East
# Post-condition: Karel reaches any position facing East
def paint_u():
    move_to_start()  # Karel reaches the starting point
    turn_left()
    for i in range(11):  # Karel paints the vertical line of U going northwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_around()
    for i in range(11):
        move()
    turn_left()
    for i in range(7):  # Karel paints the horizontal line of U going eastwards
        move()
        put_beeper()
        paint_corner(RED)
    turn_left()
    for i in range(10):  # Karel paints the vertical line of U going northwards
        move()
        put_beeper()
        paint_corner(RED)
    turn_right()


# Karel paints the letter S in the world
# Pre-condition: Karel starts at origin (1,1) facing East
# Post-condition: Karel reaches any position facing East
def paint_s():
    move_to_start()  # Karel reaches the starting point
    for i in range(7):  # Karel paints the horizontal line of S going eastwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_left()
    for i in range(5):  # Karel paints the vertical line of S going northwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_left()
    for i in range(7):  # Karel paints the horizontal line of S going westwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_right()
    for i in range(5):  # Karel paints the vertical line of S going northwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_right()
    for i in range(8):  # Karel paints the horizontal line of S going eastwards
        put_beeper()
        paint_corner(RED)
        move()


# Karel paints the letter H in the world
# Pre-condition: Karel starts at origin (1,1) facing East
# Post-condition: Karel reaches any position facing East
def paint_h():
    move_to_start()  # Karel reaches the starting point
    turn_left()
    for i in range(11):  # Karel paints the vertical line of H going northwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_around()
    for i in range(6):
        move()
    turn_left()
    for i in range(6):  # Karel paints the horizontal line of H going eastwards
        move()
        put_beeper()
        paint_corner(RED)
    move()
    turn_right()
    for i in range(5):
        move()
    turn_around()
    for i in range(11):  # Karel paints the vertical line of H going northwards
        put_beeper()
        paint_corner(RED)
        move()
    turn_right()


# Move to the starting position from where painting the letter would be started.
# Pre-condition: Karel is at origin (1,1) facing East
# Post-condition: Karel moves to (7,5) and stands facing East
def move_to_start():
    for i in range(6):
        move()
    turn_left()
    for i in range(4):
        move()
    turn_right()


# Karel moves to its origin position
# Pre-condition: Karel is at any position facing East
# Post-condition: Karel is at its origin position (1,1) facing East
def origin():
    turn_right()
    while front_is_clear():  # Karel moves to the position (1,1)
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_around()


# Karel clears the whole world by picking up all the beepers
# Pre-condition: Karel should be at the origin (1,1) facing East
# Post-condition: Karel returns to its origin (1,1) facing East
def clear_world():
    for i in range(19):
        clear_row()
        turn_right()
        move()
        turn_right()
    clear_row()  # To overcome the fencepost error
    turn_left()
    while front_is_clear():
        move()
    turn_left()


# Karel clears the whole row by picking up all the beepers in that row
# Pre-condition: Karel is at the origin (1,1) facing East
# Post-condition: Karel shifts just one position northwards from its previous position facing West
def clear_row():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            paint_corner(WHITE)
            move()
        else:
            move()
    turn_around()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            paint_corner(WHITE)
            move()
        else:
            move()


# Karel turns right by turning left three times
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Karel turns around by turning left two times
def turn_around():
    turn_left()
    turn_left()


# Karel clears the whole world by picking up all the beepers
# Pre-condition: Karel should be at the origin (1,1) facing East
# Post-condition: Karel returns to its origin (1,1) facing East
def white_world():
    for i in range(19):
        white_row()
        turn_right()
        move()
        turn_right()
    white_row()  # To overcome the fencepost error
    turn_left()
    while front_is_clear():
        move()
    turn_left()


# Karel clears the whole row by picking up all the beepers in that row
# Pre-condition: Karel is at the origin (1,1) facing East
# Post-condition: Karel shifts just one position northwards from its previous position facing West
def white_row():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            paint_corner(WHITE)
            move()
        else:
            paint_corner(WHITE)
            move()
    turn_around()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            paint_corner(WHITE)
            move()
        else:
            paint_corner(WHITE)
            move()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
