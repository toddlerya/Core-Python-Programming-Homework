#!/usr/bin/env python
# coding:utf-8
# author:toddlerya
# date:Jan 17 2015
"""
6–19.多列输出.有任意项的序列或者其他容器,把它们等距离分列显示.由调用者提供数据和
输出格式.例如,如果你传入 100 个项并定义 3 列输出,按照需要的模式显示这些数据.这种情况下,应
该是两列显示 33 个项,最后一列显示 34 个.你可以让用户来选择水平排序或者垂直排序.
"""


def reverse_matrix(a_list):
    """反转矩阵"""
    row = len(a_list)
    col = len(a_list[0])
    col_temp = []
    res_rev_matrix = []
    for c in range(col):
        for r in range(row):
            col_temp.append(a_list[r][c])
        res_rev_matrix.append(col_temp)
        col_temp = []  # 必须清空该列表，否则影响后面的数据

    " 不足的空格补'*' "
    sub = len(res_rev_matrix[0]) - (len(a_list[row - 1]) - len(a_list[row - 2]))
    if sub != len(res_rev_matrix[0]):
        res_rev_matrix.append(["*"] * sub + a_list[row - 1][col:len(a_list[row - 1])])
    return res_rev_matrix


def multi_print(b_list, line, style=True):
    length = len(b_list)
    res_matrix = []
    interval = length / line
    remainder = length % line
    if 0 == remainder:
        x = 0
        y = 0
        while y < line:
            res_matrix.append(b_list[x:x + interval])
            x += interval
            y += 1
    else:
        x = 0
        y = 0
        while y < line-1:
            res_matrix.append(b_list[x:x + interval])
            x += interval
            y += 1
        res_matrix.append(b_list[x:x + interval+remainder])
    if not style:
        return reverse_matrix(res_matrix)
    return res_matrix


if __name__ == "__main__":
    result = []
    container = []
    for i in range(1, 101):
        container.append(i)

    print "水平排序：\n"
    result = multi_print(container, 5)
    for i in result:
        print i

    print "\n\n"

    print "垂直排序：\n"
    result = multi_print(container, 8, False)
    for i in result:
        print i
