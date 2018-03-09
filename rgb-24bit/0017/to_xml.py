# -*- coding: utf-8 -*-

import json
import xlrd

from collections import OrderedDict
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom.minidom import parseString


def get_data_dict(file_name='student.xls'):
    with xlrd.open_workbook(file_name) as fp:
        sheet, data = fp.sheet_by_index(0), OrderedDict()

        for i in range(sheet.nrows):
            data[str(i + 1)] = sheet.row_values(i)[1:]

        return data


def get_xml(root, child, comment_str, data_dict):
    root = Element(root)
    root.append(Comment(text=comment_str.decode('utf-8')))

    text = json.dumps(data_dict, ensure_ascii=False, indent=4)
    SubElement(root, child).text = '\n' + text + '\n'

    return tostring(root, encoding='utf-8')


def gen_xml(file_name, xml):
    with open(file_name, 'w') as fp:
        dom = parseString(xml)
        text = dom.toprettyxml(encoding='utf-8')
        fp.write(text.replace('&quot;', '"'))


if __name__ == '__main__':
    data = get_data_dict()
    file_name = 'students.xml'
    comment = '\n\t学生信息表\n\t"id" : [名字, 数学, 语文, 英文]\n'
    xml = get_xml('root', 'students', comment, data)
    gen_xml(file_name, xml)
