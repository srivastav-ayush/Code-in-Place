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

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels

PADDLE_Y = CANVAS_HEIGHT - 40
PADDLE_WIDTH = 100

BALL_SIZE = 70

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Pong 1')

    ball = canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill='red', outline='red')
    # TODO: 1. we now make a paddle
    paddle = canvas.create_rectangle(0, PADDLE_Y, PADDLE_WIDTH, CANVAS_HEIGHT - 20, fill="blue")

    dx = 10
    dy = 7
    while True:
        # TODO: 2. get the mouse location and react to it
        mouse_x = canvas.winfo_pointerx()
        canvas.moveto(paddle, mouse_x, PADDLE_Y)

        canvas.move(ball, dx, dy)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            dx *= -1
        if hit_top_wall(canvas, ball):
            dy *= -1

        # TODO: 3. check if the ball hits the paddle
        if hit_paddle(canvas, ball, paddle):
            dy *= -1
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1/50.)

def hit_paddle(canvas, ball, paddle):
    # TODO: paddle_coords is of type list. Come to lecture Monday!
    paddle_coords = canvas.coords(paddle)
    x1 = paddle_coords[0]
    y1 = paddle_coords[1]
    x2 = paddle_coords[2]
    y2 = paddle_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)
    return len(results) > 1

def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    return get_bottom_y() >= CANVAS_HEIGHT

######## These helper methods use "lists" ###########
### Which is a concept you will learn Monday ###########

def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]

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
