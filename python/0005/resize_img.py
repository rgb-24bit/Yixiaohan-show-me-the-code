# -*- coding: utf-8 -*-

from __future__ import division

from PIL import Image

import os


def get_img_file(dir_name):
    all_img = os.listdir(dir_name)
    for img in all_img:
        yield os.path.join(dir_name, img)


def resize_img(image_file, width=640, height=1136):
    img = Image.open(image_file)
    w, h = img.size
    scale = max(w / width, h / height)

    if scale > 1:
        new_img = img.resize((int(w / scale), int(h / scale)), Image.LANCZOS)
        new_img.save('new-' + image_file)
        new_img.close()


if __name__ == '__main__':
    for img in get_img_file('image'):
        resize_img(img)
