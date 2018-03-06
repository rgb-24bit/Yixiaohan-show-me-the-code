# -*- coding: utf-8 -*-

import xlwt


def get_data(file_name='numbers.txt'):
    with open(file_name, 'r') as fp:
        return eval(fp.read())


if __name__ == '__main__':
    wb = xlwt.Workbook()
    ws = wb.add_sheet('numbers')

    for row, row_val in enumerate(get_data()):
        for col, val in enumerate(row_val):
            ws.write(row, col, val)

    wb.save('numbers.xls')
