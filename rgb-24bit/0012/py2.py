# -*- coding: utf-8 -*-

from __future__ import print_function

import sys


def get_filtered_words(file_name='filtered_words.txt'):
    with open(file_name, 'r') as fp:
        filtered_words = [word.strip() for word in fp]
    return filtered_words


def get_user_input():
    return raw_input('Input: ').decode(sys.stdin.encoding).encode('utf-8')


def prog_output(user_input, filtered_words):
    for word in filtered_words:
        user_input = user_input.replace(word, '*' * len(word.decode('utf-8')))  # decode('utf-8') 解决中文长度问题
    print(user_input.decode('utf-8').encode(sys.stdout.encoding))


if __name__ == '__main__':
    filtered_words = get_filtered_words()
    prog_output(get_user_input(), filtered_words)
