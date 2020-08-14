"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""


import tkinter
import time
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 400     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Random Circles')

    for i in range(50):
        random_circle(canvas)
    canvas.mainloop()

def random_circle(canvas):
    diameter = random.randint(50, 100)
    color = random.choice(['blue', 'salmon', 'red', 'green', 'orange', 'plum'])
    x = random.randint(0, CANVAS_WIDTH - diameter)
    y = random.randint(0, CANVAS_HEIGHT - diameter)
    canvas.create_oval(x, y, x + diameter, y + diameter, fill=color, outline=color)

def mouse_pressed(event, canvas):
    print('mouse pressed', event.x, event.y)
    x = event.x
    y = event.y
    found = canvas.find_overlapping(x, y, x, y)
    if len(found) > 0:
        canvas.delete(found[-1])

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
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    canvas.bind("<Button-1>", lambda e: mouse_pressed(e,canvas))
    return canvas




if __name__ == '__main__':
    main()
