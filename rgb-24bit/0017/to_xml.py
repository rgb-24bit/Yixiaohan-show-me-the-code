# -*- coding: utf-8 -*-

import json
import xlrd

from lxml import etree
from collections import OrderedDict


def get_data_dict(file_name='student.xls'):
    with xlrd.open_workbook(file_name) as fp:
        sheet, data_dict = fp.sheet_by_index(0), OrderedDict()

        for i in range(sheet.nrows):
            data_dict[str(i + 1)] = sheet.row_values(i)[1:]

        return data_dict


def get_xml(file_name, root, child, comment_str, data_dict):
    root = etree.Element(root)
    students = etree.SubElement(root, child)

    comment = etree.Comment(comment_str)
    comment.tail = json.dumps(data_dict, ensure_ascii=False)

    students.append(comment)

    tree = etree.ElementTree(root)
    tree.write(file_name, pretty_print=True, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    data_dict = get_data_dict()
    comment = u'学生信息表"id" : [名字, 数学, 语文, 英文]'
    get_xml('students.xml', 'root', 'students', comment, data_dict)
