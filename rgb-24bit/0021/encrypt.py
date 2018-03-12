# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

from hashlib import sha256


def encrypt_pwd(pwd):
    return sha256(pwd).hexdigest()


def get_pwd():
    try:
        pwd = raw_input('Input password: ').decode(sys.stdin.encoding)
        pwd = pwd.encode('utf-8')
    except NameError:
        pwd = input('Input password: ').encode('utf-8')

    return pwd

if __name__ == '__main__':
    print(encrypt_pwd(get_pwd()))
