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
SQUARE_SIZE = 70

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Move Square')
    # make the rectangle...
    start_y = CANVAS_HEIGHT / 2 - SQUARE_SIZE / 2
    end_y = start_y + SQUARE_SIZE
    rect = canvas.create_rectangle(0, start_y, SQUARE_SIZE, end_y, fill='black')

    # animation loop
    while not is_past_middle(canvas, rect):
        # update the world
        canvas.move(rect, 1, 0)
        canvas.update()

        # pause
        time.sleep(1/50.) #parameter is seconds to pause.
    canvas.mainloop()

def is_past_middle(canvas, rect):
    max_x = CANVAS_WIDTH / 2 - SQUARE_SIZE / 2
    curr_x = get_left_x(canvas, rect)
    return curr_x > max_x

######## These helper methods use "lists" ###########
### Which is a concept you will learn Monday ###########

def get_left_x(canvas, shape):
    # returns the x location of the shape
    return canvas.coords(shape)[0]

def get_top_y(canvas, shape):
    # returns the y location of the shape
    return canvas.coords(shape)[1]


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
