from simpleimage import SimpleImage

RGB_MAX = 255  # Max RGB value. 255 for 24-bit RGB image
BLUR_SIZE = 11  # Size of the box filter. Should be positive odd integer
BLUR_ITER = 15  # Number of iterations of box filtering.


def main():
    img = SimpleImage('images/ayush.jpeg')
    img.show()

    gray = convert_to_gray(img)
    gray.show()

    inverted = invert_color(gray)
    inverted.show()

    blurred = blur(inverted, BLUR_ITER, BLUR_SIZE)
    blurred.show()

    pencil = dodge(gray, blurred)
    pencil.show()


def dodge(top, bottom):
    """
    Returns a new SimpleImage object, which is a doge blending of two
    SimpleImage objects: top and bottom. In the dodge mode, we divide
    the bottom layer RGB by the inverted top layer RGB.
    See https://en.wikipedia.org/wiki/Blend_modes for more information.
    """
    img = copy_image(top)
    for px in img:
        x = px.x
        y = px.y
        px_top = top.get_pixel(x, y)
        px_bottom = bottom.get_pixel(x, y)
        px.red = compute_dodge(px_top.red, px_bottom.red)
        px.green = compute_dodge(px_top.green, px_bottom.green)
        px.blue = compute_dodge(px_top.blue, px_bottom.blue)
    return img


def compute_dodge(top_val, bottom_val):
    """
    Helper function for the actual computation.
    Uses max(1,..) to prevent division by zero
    """
    val = bottom_val * RGB_MAX / max(1, RGB_MAX - top_val)
    return min(val, RGB_MAX)


def blur(img, num_iter, blur_size):
    """
    Returns a new SimplgeImage object, which is a blurred version
    of SimpleImage img. Uses box filters: box size is blur_size
    and the filtering is performed num_iter times. The implementation
    is not the most efficient, so long computing time may be expected
    for large image dimension, larger num_iter, or large blur_size.
    blur_size is a positive odd integer.
    num_iter is a positive integer.
    """
    ref = img
    for i in range(num_iter):
        blurred = copy_image(ref)
        for x in range(ref.width):
            for y in range(ref.height):
                blur_pixel(x, y, blurred, ref, blur_size)
        ref = blurred
    return blurred


def blur_pixel(x, y, blurred, ref, blur_size):
    """
    Update the RGB values of a pixel in SimpleImage 'blurred' at
    coordinates (x, y). The RGB value is the box average of pixels
    in SimpleImage 'ref'. The box is a square centered at (x, y)
    with side length blur_size.
    Note that 'blurred' is modified while 'ref' remains unchanged.
    These two images must have the same dimension.
    Parameters x, y are nonnegative integers within the boundary of
    the image. blur_size is a positive odd integer.
    """
    red = 0
    blue = 0
    green = 0
    count = 0
    r = (blur_size - 1) // 2
    for i in range(x - r, x + r + 1):
        for j in range(y - r, y + r + 1):
            if in_bound(i, j, ref.width, ref.height):
                count += 1
                px = ref.get_pixel(i, j)
                red += px.red
                blue += px.blue
                green += px.green
    pixel = blurred.get_pixel(x, y)
    pixel.red = red / count
    pixel.green = green / count
    pixel.blue = blue / count


def in_bound(x, y, width, height):
    """
    Returns True if the given pixel coordinates (x, y)
    is located inside the image with dimension (width, height).
    Returns False otherwise.
    All parameters are integers
    """
    if 0 <= x < width and 0 <= y < height:
        return True
    return False


def invert_color(img):
    """
    Returns a new SimpleImage object, which has an inverted
    color compared to img.
    """
    inverted = copy_image(img)
    for pixel in inverted:
        pixel.red = RGB_MAX - pixel.red
        pixel.blue = RGB_MAX - pixel.blue
        pixel.green = RGB_MAX - pixel.green
    return inverted


def convert_to_gray(img):
    """
    Returns a new SimpleImage object, which is the grayscale version
    of img. Conversion formula follows CCIR 601, see:
    https://en.wikipedia.org/wiki/Luma_(video)
    """
    copy = copy_image(img)
    for pixel in copy:
        val = 0.299 * pixel.red + 0.587 * pixel.green + 0.114 * pixel.blue
        pixel.red = val
        pixel.green = val
        pixel.blue = val
    return copy


def copy_image(img):
    """
    Returns a new SimpleImage object, which has the same
    pixel values as img, which is also a SimpleImage object
    """
    copy = SimpleImage.blank(img.width, img.height)
    for pixel in copy:
        x = pixel.x
        y = pixel.y
        copy.set_pixel(x, y, img.get_pixel(x, y))
    return copy


if __name__ == '__main__':
    main()