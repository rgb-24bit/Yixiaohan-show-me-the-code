# -*- coding: utf-8 -*-

from __future__ import print_function

import re


def get_text(file_name='words.txt'):
    with open(file_name, 'r') as fp:
        return fp.read()


def get_word_count(text):
    pattern = r'\b\w+?\b'
    return len(re.findall(pattern, text))


if __name__ == '__main__':
    text = get_text()
    print(get_word_count(text))
