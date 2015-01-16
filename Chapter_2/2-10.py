#! /usr/bin/env python
#coding: utf-8 
'''
带 循 环 和条件判断的用 户输入使用raw_input()函数来提示用户输入一个1 和 100 之间的
数,如果用户输入的数满足这个条件, 显示成功并退出。否则显示一个错误信息然后再次提示
用户输入数值 ,直到满足条件为止。
'''
get_num = ""
get_num = input("请输入一个1-100之间的数: ")
running = True
print type(get_num)
while running:
    if (1 <= get_num <= 100):
        print '成功'
        running = False
    else:
        print "输入错误，不符合要求区间"
        get_num = input("请输入一个1-100之间的数: ")
