from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
When you finish writing this file, TripleKarel should be
able to paint the exterior of three buildings in a given
world, as described in the Assignment 1 handout. You
should make sure that your program works for all of the 
Triple sample worlds supplied in the starter folder.
"""


def main():
    # Karel starts at the top right corner of the rectangle always facing west.

    # Painting the first wall.
    paint_wall()
    # When the wall ends Karel turns around and aligns with the adjacent wall.
    align_adjacent_wall()

    # Painting the second wall.
    paint_wall()
    # When the wall ends Karel turns around and aligns with the adjacent wall.
    align_adjacent_wall()

    # Painting the third wall.
    paint_wall()
    # When the wall ends, it marks the end of a rectangle.
    # Then Karel has to align with the wall of the next rectangle.
    align_next_rectangle()

    # Painting the fourth wall.
    paint_wall()
    # When the wall ends Karel turns around and aligns with the adjacent wall.
    align_adjacent_wall()

    # Painting the fifth wall.
    paint_wall()
    # When the wall ends Karel turns around and aligns with the adjacent wall.
    align_adjacent_wall()

    # Painting the sixth wall.
    paint_wall()
    # When the wall ends, it marks the end of a rectangle.
    # Then Karel has to align with the wall of the next rectangle.
    align_next_rectangle()

    # Painting the seventh wall.
    paint_wall()
    # When the wall ends Karel turns around and aligns with the adjacent wall.
    align_adjacent_wall()

    # Painting the eight wall.
    paint_wall()
    # When the wall ends Karel turns around and aligns with the adjacent wall.
    align_adjacent_wall()

    # Painting the ninth wall.
    paint_wall()


def paint_wall():
    while left_is_blocked():
        put_beeper()
        move()


def align_adjacent_wall():
    turn_left()
    move()


def align_next_rectangle():
    turn_left()
    turn_left()
    turn_left()


# Karel stops and the task assigned to Karel has been completed.

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
