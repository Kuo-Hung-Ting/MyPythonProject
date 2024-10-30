"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            count = 0
            total_r = 0
            total_b = 0
            total_g = 0
            for left_right in range(-1,2):
                for up_down in range(-1,2):
                    if img.width > x + left_right > 0 and 0 < y+up_down < img.height:
                        img_p = img.get_pixel(x + left_right, y + up_down)
                        count += 1
                        total_r += img_p.red
                        total_b += img_p.blue
                        total_g += img_p.green
            img_k = new_img.get_pixel(x,y)
            img_k.red = total_r / count
            img_k.green = total_g / count
            img_k.blue = total_b / count
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
