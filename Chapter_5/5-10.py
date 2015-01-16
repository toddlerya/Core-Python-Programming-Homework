#!/usr/bin/env python
#coding:utf-8
 
"""
5-10 转换。写一对函数来进行华氏度到摄氏度的转换。转换公式为 C = (F - 32) * (5 / 9)
应该在这个练习中使用真正的除法, 否则你会得到不正确的结果。
"""
# 精确除法
from __future__ import division 

 
def F_to_C():
    F_temp = raw_input('请输入华氏温度：')    
    C_temp_result = (eval(F_temp) - 32) * (5 / 9) 
    return '华氏温度转换为摄氏温度---->' + str(C_temp_result)

 
def C_to_F():
    C_temp = raw_input('请输入摄氏温度：')
    F_temp_result = (eval(C_temp)) / (5 / 9) + 32
    return '摄氏温度转换为华氏温度---->' + str(F_temp_result)

 
def choose():
    choice = raw_input('请选择转换方式：1-华氏--->摄氏，2-摄氏--->华氏（请输入序号）')
    if choice == '1':
        print F_to_C()
    elif choice == '2':
        print C_to_F()
    else:
        return '请输入正确的选项'
        choose()
 
 
 if __name__ == "__main__":
    choose()
