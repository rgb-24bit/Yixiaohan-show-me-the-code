# -*- coding: utf-8 -*-

import xlrd

from collections import OrderedDict
from xml.dom import minidom, Node


def get_data(file_name='student.xls'):
    with xlrd.open_workbook(file_name) as fp:
        sheet = fp.sheet_by_index(0)
        data = dict()

        for i in range(sheet.nrows):
            data[str(i+1)] = sheet.row_values(i)[1:]

        return data


def gen_xml(file_name, root, child, comment, data):
    impl = minidom.getDOMImplementation()
    new_doc = impl.createDocument(None, root, None)

    node_students = new_doc.createElement(child)
    node_students.appendChild(new_doc.createComment(comment))
    node_students.appendChild(new_doc.createTextNode(data))

    node_root = new_doc.documentElement
    node_root.appendChild(node_students)

    with open(file_name, 'w') as fp:
        new_doc.writexml(fp, newl='\n')



if __name__ == '__main__':
    data = get_data()
    file_name = 'students.xml'
    comment = '\n\t学生信息表\n\t"id" : [名字, 数学, 语文, 英文]\n'
    gen_xml(file_name, 'root', 'students', comment, str(data))
