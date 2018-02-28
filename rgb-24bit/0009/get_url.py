# -*- coding: utf-8 -*-

import re
import io


def get_html(file_name):
    with io.open(file_name, 'r', encoding='utf-8') as fp:
        return fp.read()


def get_url(html):
    pattern = r'http[s]?://[\w.-/]+'
    return re.findall(pattern, html)


if __name__ == '__main__':
    html = get_html('web.html')
    with io.open('results.txt', 'w', encoding='utf-8') as fp:
        for url in get_url(html):
            fp.write(url + '\n')
