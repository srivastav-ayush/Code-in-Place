"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():

    # Creating a blank image of size which can fit in 6 patch images
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # Creating 6 patch images with different filters
    patch11 = make_recolored_patch(1, 0, 2)
    patch12 = make_recolored_patch(5, 8, 1.3)
    patch13 = make_recolored_patch(1, 3, 7)
    patch21 = make_recolored_patch(1.2, 0.1, 1.9)
    patch22 = make_recolored_patch(9, 0.3, 4)
    patch23 = make_recolored_patch(5, 0.2, 6)

    # Input patch11 in the final image
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            pixel = patch11.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)

    # Input patch12 in the final image
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            pixel = patch12.get_pixel(x, y)
            final_image.set_pixel(x+222, y, pixel)

    # Input patch13 in the final image
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            pixel = patch13.get_pixel(x, y)
            final_image.set_pixel(x+444, y, pixel)

    # Input patch21 in the final image
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            pixel = patch21.get_pixel(x, y)
            final_image.set_pixel(x, y+222, pixel)

    # Input patch22 in the final image
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            pixel = patch22.get_pixel(x, y)
            final_image.set_pixel(x+222, y+222, pixel)

    # Input patch23 in the final image
    for x in range(PATCH_SIZE):
        for y in range(PATCH_SIZE):
            pixel = patch23.get_pixel(x, y)
            final_image.set_pixel(x+444, y+222, pixel)

    # Showing the final image with all the patches
    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    """
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red = pixel.red * red_scale
        pixel.green = pixel.green * green_scale
        pixel.blue = pixel.blue * blue_scale
    return patch

if __name__ == '__main__':
    main()