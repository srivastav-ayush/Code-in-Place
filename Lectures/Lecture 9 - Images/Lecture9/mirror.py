"""
File: mirror.py
---------------
This program shows an example of creating an image
that shows an original image and its mirror reflection
in a new image.
"""


from simpleimage import SimpleImage


def mirror_image(filename):
    """
    Read an image from the file specified by filename.
    Returns a new images that includes the original image
    and its mirror reflection.
    Returns the resulting "redscreened" image.
    """
    image = SimpleImage(filename)
    width = image.width
    height = image.height

    # Create new image to contain mirror reflection
    mirror = SimpleImage.blank(width * 2, height)

    for y in range(height):
        for x in range(width):
            pixel = image.get_pixel(x, y)
            mirror.set_pixel(x, y, pixel)
            mirror.set_pixel((width * 2) - (x + 1), y, pixel)
    return mirror


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    original = SimpleImage('images/burrito.jpg')
    original.show()

    mirrored = mirror_image('images/burrito.jpg')
    mirrored.show()


if __name__ == '__main__':
    main()
