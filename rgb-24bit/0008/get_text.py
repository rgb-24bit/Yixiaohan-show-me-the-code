# -*- coding: utf-8 -*-

from __future__ import print_function

import io

try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser


class MyHTMLParse(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.text = list()
        self.cur_tag = None

    def handle_starttag(self, tag, attrs):
        self.cur_tag = tag

    def handle_data(self, data):
        if self.cur_tag not in ('script', 'style') and data.strip():
            self.text.append(data.strip())

    def get_text(self):
        return self.text


def get_html(file_name):
    with io.open(file_name, 'r', encoding='utf-8') as fp:
        return fp.read()


if __name__ == '__main__':
    html = get_html('web.html')
    parser = MyHTMLParse()
    parser.feed(html)

    with io.open('result.txt', 'w', encoding='utf-8') as fp:
        for text in parser.get_text():
            fp.write(text + '\n')
