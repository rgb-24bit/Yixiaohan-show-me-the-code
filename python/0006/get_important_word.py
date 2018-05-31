# -*- coding: utf-8 -*-

from __future__ import print_function

import re
import os


def get_text(dir_name='diary'):
    diary_lst = os.listdir(dir_name)
    for diary in diary_lst:
        with open(os.path.join(dir_name, diary), 'r') as fp:
            yield (diary, fp.read())


def get_important_word(text):
    pattern = r'\b\w+?\b'
    all_word = re.findall(pattern, text)

    d = dict()
    for word in all_word:
        d[word] = d.get(word, 0) + 1

    res, max_count = list(), max(d.values())
    for k, v in d.items():
        if v == max_count:
            res.append(k)

    return res


if __name__ == '__main__':
    for diary, text in get_text():
        print(diary, ' '.join(get_important_word(text)))
