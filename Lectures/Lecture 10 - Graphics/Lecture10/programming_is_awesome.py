"""
File: pyramid.py
----------------
YOUR DESCRIPTION HERE
"""


import tkinter
import time
import random
from PIL import ImageTk
from PIL import Image

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Awesome')
    # a line for good measure!
    canvas.create_line(0, 0, 600, 600)

    # a blue square with width and height = 80
    canvas.create_rectangle(70, 70, 150, 150, fill="blue")
    # a yellow rectangle that is long and skinny
    canvas.create_rectangle(620, 100, 640, 510, fill="yellow")

    # a red oval and a rectangle at the exact same spot!
    canvas.create_rectangle(250, 150, 500, 500)
    canvas.create_oval     (250, 150, 500, 500, fill="red", outline="red")

    # images require the pillow library
    image = ImageTk.PhotoImage(Image.open("images/simba.png"))
    canvas.create_image(0,300,anchor="nw",image=image)

    # some text is written on the screen.
    canvas.create_text(20, 200, anchor='w', font='Courier 52', text='Programming is Awesome!')

    # dude, where's my rect?
    canvas.create_rectangle(0, 800, 10, 810)
    canvas.mainloop()


def mouse_moved(event):
    print('x = ' + str(event.x), 'y = ' + str(event.y))

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

    canvas.bind("<Motion>", mouse_moved)
    return canvas




if __name__ == '__main__':
    main()
