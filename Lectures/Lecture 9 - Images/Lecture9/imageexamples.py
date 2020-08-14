"""
File: imageexample.py
---------------------
This program contains several examples of functions that
manipulate an image to show how the SimpleImage library works.
"""


from simpleimage import SimpleImage


def darker(filename):
    """
    Reads image from file specified by filename.
    Makes image darker by halving red, green, blue values.
    Returns the darker version of image.
    """
    # Demonstrate looping over all the pixels of an image,
    # changing each pixel to be half its original intensity.
    image = SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
    return image


def red_channel(filename):
    """
    Reads image from file specified by filename.
    Changes the image as follows:
    For every pixel, set green and blue values to 0
    yielding the red channel.
    Return the changed image.
    """
    image = SimpleImage(filename)
    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
    return image


def right_half_darker(filename):
    """
    Reads image from file specified by filename.
    Make *right half* of the image to be half as bright.
    (Show an example setting RGB values as floats)
    """
    image = SimpleImage(filename)
    for pixel in image:
        # if pixel is in right half of image
        # (e.g. width is 100, right half begins at x=50)
        if pixel.x >= image.width // 2:
            pixel.red *= 0.5
            pixel.green *= 0.5
            pixel.blue *= 0.5
    return image


def compute_luminosity(red, green, blue):
    """
    Calculates the luminosity of a pixel using NTSC formula
    to weight red, green, and blue values appropriately.
    """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)


def grayscale(filename):
    """
    Reads image from file specified by filename.
    Change the image to be grayscale using the NTSC
    luminosity formula and return it.
    """
    image = SimpleImage(filename)
    for pixel in image:
        luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity
    return image


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    original_flower = SimpleImage('images/wallpaper.jpg')
    original_flower.show()

    dark_flower = darker('images/wallpaper.jpg')
    dark_flower.show()

    red_flower = red_channel('images/wallpaper.jpg')
    red_flower.show()

    """
    grayscale_flower_avg = grayscale('images/flower.png')
    grayscale_flower_avg.show()
    """

if __name__ == '__main__':
    main()
