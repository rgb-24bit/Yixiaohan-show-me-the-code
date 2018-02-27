# -*- coding: utf-8 -*-

from __future__ import print_function

import os
import io


def get_file_list(dir_name):
    file_type = '.py'
    for file_name in os.listdir(dir_name):
        if file_type == os.path.splitext(file_name)[-1]:
            yield os.path.join(dir_name, file_name)


def get_code_amount(file_name):
    key = ['code', 'blank', 'comment']
    code_amount = dict.fromkeys(key, 0)

    with io.open(file_name, 'r', encoding='utf-8') as fp:
        for line in fp:
            if line.strip():
                if line[0] == '#':
                    code_amount['comment'] += 1
                else:
                    code_amount['code'] += 1
            else:
                code_amount['blank'] += 1

    return code_amount


if __name__ == '__main__':
    key = ['code', 'blank', 'comment']
    all_code_amount = dict.fromkeys(key, 0)

    for file_name in get_file_list('../0012'):
        code_amount = get_code_amount(file_name)
        for key, val in code_amount.items():
            all_code_amount[key] += val

    for key, val in all_code_amount.items():
        print(key, val)
