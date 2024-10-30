"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
import math
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = math.sqrt(math.pow((red-pixel.red),2)+math.sqrt(math.pow((green-pixel.green),2))+math.sqrt(math.pow((blue-pixel.blue),2)))
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    rgb = []
    red = 0
    green = 0
    blue = 0
    amount = len(pixels)
    for i in range(amount):
        red += pixels[i].red
        green += pixels[i].green
        blue += pixels[i].blue
    rgb.append(red//amount)
    rgb.append(green//amount)
    rgb.append(blue//amount)
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    amount = len(pixels)
    avg = get_average(pixels)
    dist = get_pixel_dist(pixels[0], avg[0], avg[1], avg[2])
    best = dist
    best_pixel = pixels[0]
    for i in range(amount-1):
        dist = get_pixel_dist(pixels[i+1], avg[0], avg[1], avg[2])
        if dist < best:
            best = dist
            best_pixel = pixels[i+1]
    return best_pixel





def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    amount = len(images)
    for x in range(width):
        for y in range(height):
            pixels = []
            for h in range(amount):
                pixel = images[h].get_pixel(x,y)
                pixels.append(pixel)
            best_pixel = get_best_pixel(pixels)
            result_p = result.get_pixel(x,y)
            result_p.red = best_pixel.red
            result_p.green = best_pixel.green
            result_p.blue = best_pixel.blue



    # ----- YOUR CODE ENDS HERE ----- #


    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
