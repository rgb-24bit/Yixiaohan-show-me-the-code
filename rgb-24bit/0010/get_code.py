# -*- coding: utf-8 -*-

import string
import random

from PIL import Image, ImageFont, ImageDraw, ImageFilter


def get_rand_char():
    return random.choice(string.ascii_letters)


def get_bg_color():
    rand = random.randint
    return (rand(102, 204), rand(102, 255), rand(204, 255))


def get_font_color():
    rand = random.randint
    return (rand(32, 127), rand(32, 127), rand(32, 127))


def get_code():
    width, height = 60 * 4, 60
    image = Image.new('RGB', (width, height), (25, 255, 255))
    font = ImageFont.truetype('arial.ttf', 36)
    darw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            darw.point((x, y), fill=get_bg_color())

    for i in range(4):
        darw.text((i * 60 + 10, 10), get_rand_char(), font=font, fill=get_bg_color())


    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')


if __name__ == '__main__':
    get_code()
