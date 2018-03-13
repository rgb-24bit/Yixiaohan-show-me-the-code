# -*- coding: utf-8 -*-

from __future__ import print_function

import io
import os
import sys

from hashlib import sha256
from hmac import HMAC

def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8)

    for i in range(10):
        try:
            password = HMAC(password, salt, sha256).hexdigest().encode('utf-8')  # python3 的返回值是 unicode
        except TypeError:
            password = HMAC(password, salt, sha256).hexdigest()

    return salt + password  # 保存每个账号的 salt



def get_password():
    try:
        password = raw_input('Input password: ').decode(sys.stdin.encoding)
        password = password.encode('utf-8')
    except NameError:
        password = input('Input password: ').encode('utf-8')

    return password


if __name__ == '__main__':
    print(encrypt_password(get_password()))
