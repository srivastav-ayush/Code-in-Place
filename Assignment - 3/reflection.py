"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""

# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):

    # Getting the original image's height & width and modifying it for the new image
    image = SimpleImage(filename)
    h = image.height
    w = image.width
    new_h = 2 * h
    new_w = w

    # Creating a blank image with a size of twice the height of the original image
    image_new = SimpleImage.blank(new_w, new_h)

    # Creating a loop to get all the individual pixels and copy them to a mirror location to get the mirrored image
    for x in range(w):
        for y in range(h):
            pixel = image.get_pixel(x, y)
            image_new.set_pixel(x, y, pixel)
            image_new.set_pixel(x, new_h-(y+1), pixel)
    return image_new


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
