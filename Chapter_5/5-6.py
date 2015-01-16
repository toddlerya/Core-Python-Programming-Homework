#!/usr/bin/env python
#coding: utf-8

"""
5-6 算术。写一个计算器程序你的代码可以接受这样的表达式,两个操作数加一个运算符:
N1 运算符 N2. 其中 N1 和 N2 为整数或浮点数,运算符可以是+, -, *, /, %, ** 分别表示
加法,减法, 乘法, 整数除,取余和幂运算。计算这个表达式的结果,然后显示出来。提示:
可以使用字符串方法 split(),但不可以使用内建函数 eval().
"""
 
import types
 
 
def calc(expression):
    operator = ['+','-','*','/','%','**']    
    ope = '' 
 
    if not type(expression) is types.StringType:
        print '请输入正确的表达式，例如：1 + 2'
        return 
                 
    for o in operator:
        if o in expression:
            ope = o
 
    if ope == '':
        print '运算符错误'
        return
 
   # print ope
    number = expression.split(ope)
    arg_1 = number[0]
    arg_2 = number[1]
    list_1 = list(arg_1)
    list_2 = list(arg_2)
    if '.' in list_1:
        num_1 = float(arg_1)
    else:
        num_1 = int(arg_1)
    if '.' in list_2:
        num_2 = float(arg_2)
    else:
        num_2 = int(arg_2)
 
    if ope == operator[0]:
        return "%s = %f" % (expression, num_1 + num_2)
    if ope == operator[1]:
        return "%s = %f" % (expression, num_1 - num_2)
    if ope == operator[2]:
        return "%s = %f" % (expression, num_1 * num_2)
    if ope == operator[3]:
        return "%s = %f" % (expression, num_1 / num_2)
    if ope == operator[4]:
        return "%s = %f" % (expression, num_1 % num_2)
    if ope == operatro[5]:
        return "%s = %f" % (expression, num_1 ** num_2)
 
expression = raw_input('请输入你的运算表达式（例如：1 + 2）：')
print calc(expression)
