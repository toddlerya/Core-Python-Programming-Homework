#! /usr/bin/env python
# coding: utf-8
 
"""
6–13.字符串.string 模块包含三个函数,atoi(),atol(),和 atof(),它们分别负责把字符串转
换成整数,长整型,和浮点型数字.从 Python1.5 起,Python 的内建函数 int(),long(),float()也可以
做相同的事了, complex()函数可以把字符串转换成复数.(然而 1,5 之前,这些转换函数只能工作于
数字之上)
string 模块中并没有实现一个 atoc()函数,那么你来实现一个,atoc(),接受单个字符串做参
数输入,一个表示复数的字符串,例如,'-1.23e+4-5.67j',返回相应的复数对象.你不能用 eval()函
数,但可以使用 complex()函数,而且你只能在如下的限制之下使用 complex():complex(real,imag)
的 real 和 imag 都必须是浮点值.
"""
 
 
def atoc(string):
    flag_index = string.rfind('-')
    if flag_index <= 0:
        flag_index = string.rfind('+')
    if flag_index > 0:
        real = float(string[0:flag_index])
        imag = float(string[flag_index:-1])
    return complex(real,imag)
 
print atoc('-1.23e+4-5.67j')
