# -*- coding: utf-8 -*-

import json
import xlwt

from collections import OrderedDict


def get_data(file_name='city.txt'):
    with open(file_name, 'r') as fp:
        for key, val in json.load(fp, object_pairs_hook=OrderedDict).items():
            yield (key, val)


if __name__ == '__main__':
    wb = xlwt.Workbook()
    ws = wb.add_sheet('city')

    for row, row_val in enumerate(get_data()):
        for col, val in enumerate(row_val):
            ws.write(row, col, val)

    wb.save('city.xls')
