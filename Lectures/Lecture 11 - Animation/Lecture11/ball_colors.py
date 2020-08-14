"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""

import tkinter
import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

CANVAS_WIDTH = 600  # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600  # Height of drawing canvas in pixels

BALL_SIZE = 70


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Bouncing Ball')

    ball = canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill='blue', outline='blue')

    dx = 10
    dy = 7
    while True:
        # update world
        canvas.move(ball, dx, dy)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
            change_color(canvas, ball)
        if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
            dy *= -1
            change_color(canvas, ball)
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1 / 50.)


def change_color(canvas, shape):
    '''
    When you call this method, the provided shape will change color to a
    randomly chosen color.
    :param canvas: the canvas where the shape exists
    :param shape: the shape you want to have its color changed
    '''
    # 1. get a random color
    color = random.choice(['blue', 'salmon', 'red', 'green', 'orange', 'plum'])
    # 2. use the tkinter method to change the shape's color
    canvas.itemconfig(object, fill=color, outline=color)  # change color


def hit_left_wall(canvas, object):
    return canvas.coords(object)[0] <= 0


def hit_top_wall(canvas, object):
    return canvas.coords(object)[1] <= 0


def hit_right_wall(canvas, object):
    return canvas.coords(object)[2] >= CANVAS_WIDTH


def hit_bottom_wall(canvas, object):
    return canvas.coords(object)[3] >= CANVAS_HEIGHT


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == '__main__':
    main()
