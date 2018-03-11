# -*- coding: utf-8 -*-

import xlrd

from lxml import etree


def get_data_list(file_name='numbers.xls'):
    with xlrd.open_workbook(file_name) as fp:
        sheet, data_list = fp.sheet_by_index(0), list()

        for i in range(sheet.nrows):
            row = [int(val) for val in sheet.row_values(i)]
            data_list.append(row)

        return data_list


def get_xml(file_name, root, child, comment_str, data_list):
    root = etree.Element(root)
    students = etree.SubElement(root, child)

    comment = etree.Comment(comment_str)
    comment.tail = str(data_list).decode('utf-8')

    students.append(comment)

    tree = etree.ElementTree(root)
    tree.write(file_name, pretty_print=True, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    data_list = get_data_list()
    comment = u'数字信息'
    get_xml('numbers.xml', 'root', 'numbers', comment, data_list)
