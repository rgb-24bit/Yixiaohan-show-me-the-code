# -*- coding: utf-8 -*-

import json
import xlwt


def get_data(file_name='student.txt'):
    with open(file_name, 'r') as fp:
        data = list()
        for key, val in json.load(fp).items():
            data.append(list(key) + val)

    return sorted(data, key=lambda x: int(x[0]))



if __name__ == '__main__':
    wb = xlwt.Workbook()
    ws = wb.add_sheet('student')

    data = get_data()
    for row in range(len(data)):
        for col in range(len(data[row])):
            ws.write(row, col, data[row][col])

    wb.save('student.xls')
