# -*- coding: utf-8 -*-

from __future__ import print_function

import re

from urllib2 import urlopen, Request, URLError


def download(url, user_agent=None, num_retries=2):
    if user_agent:
        headers = {'User-Agent': user_agent}
    else:
        headers = dict()

    req = Request(url, headers=headers)

    try:
        return urlopen(req).read()
    except URLError as e:
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, user_agent, num_retries-1)


def get_img_url(html):
    pattern = r'http://imgsrc.baidu.com/forum/.+?jpg'
    return re.findall(pattern, html)



if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'

    html = download(url, user_agent)
    all_img_url = get_img_url(html)

    for i, img_url in enumerate(all_img_url):
        img_name = '{0}.jpg'.format(i)
        print('Download', img_name)
        with open(img_name, 'wb') as fp:
            img = download(img_url, user_agent)
            fp.write(img)
