# -*- coding: utf-8 -*-

import string
import random


def get_base_str():
    return string.ascii_letters + string.digits


def get_all_code(base_str, key_len=20, key_num=200):
    def get_one_code(base_str, key_len):
        lst = [random.choice(base_str) for i in range(key_len)]
        return ''.join(lst)

    all_code = list()
    while len(all_code) < key_num:
        code = get_one_code(base_str, key_len)
        if code not in all_code:
            all_code.append(code)

    return all_code


def save_code(codes, file_name='active_code.txt'):
    with open(file_name, 'w+') as fp:
        for code in codes:
            fp.write(code + '\n')


if __name__ == '__main__':
    base_str = get_base_str()
    codes = get_all_code(base_str)
    save_code(codes)
