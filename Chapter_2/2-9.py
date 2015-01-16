#! /usr/bin/env python
#coding: utf-8
 
'''
循 环 和运算符 创 建一个包含五个固定数 值 的列表或元 组 , 输 出他 们 的平均 值 。本 练习 的 难
点之一是通 过 除法得到平均 值 。 你会 发现 整数除会截去小数,因此你必 须 使用浮点除以得到更
精确的 结 果。 float()内建函数可以帮助你 实现这 一功能。
'''
 
a_for_list = [3,2,3,3,2]
for_sum = 0
for j in a_for_list:
    for_sum = for_sum + j
print for_sum
avg = float(for_sum) / len(a_for_list)
print avg
 
 
'''
只要被参与运算的数值中有一个是float型就可以
