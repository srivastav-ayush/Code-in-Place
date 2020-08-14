"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""


import tkinter
import time
import random

WIDTH = 800
HEIGHT = 600
SIZE = 100

def main():
    canvas = make_canvas(WIDTH, HEIGHT, 'First Rectangle')

    x = (WIDTH - SIZE) / 2
    y = (HEIGHT - SIZE) / 2
    canvas.create_rectangle(x, y, x + SIZE, y + SIZE, fill="blue")
    canvas.mainloop()


######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas




if __name__ == '__main__':
    main()
