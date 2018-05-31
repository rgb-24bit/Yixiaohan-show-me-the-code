# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


def get_img(img_name):
    return Image.open(img_name)


def get_font(img, font_name):
    return ImageFont.truetype(font_name, img.height / 5)


def draw_num(img, font, num):
    w, h = img.size
    draw = ImageDraw.Draw(img)
    draw.text((w / 5 * 4, h / 5), str(num), fill=(102, 204, 255), font=font)
    return img


if __name__ == '__main__':
    img = get_img('avatar.jpg')
    font = get_font(img, 'arial.ttf')
    draw_num(img, font, 6).save('new.jpg')
