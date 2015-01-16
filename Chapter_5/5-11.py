#!/usr/bin/env python
#coding: utf-8
 
"""
5-11 取余。
(a) 使用循环和算术运算,求出 0-20 之间的所有偶数
(b) 同上,不过这次输出所有的奇数
(c) 综合 (a) 和 (b), 请问辨别奇数和偶数的最简单的方法是什么?
(d) 使用(c)的成果,写一个函数,检测一个整数能否被另一个整数整除。 先要求用户输
入两个数,然后你的函数判断两者是否有整除关系,根据判断结果分别返回 True 和 False;
"""
 
import types
 
#(a)
print '*'*5+'题目(a)'+'*'*5
for x in range(21):
    if x % 2 == 0:
        print x,
 
 
#(b)
print '\n'+'*'*5+'题目(b)'+'*'*5
for y in range(21):
    if not y % 2 == 0:
        print y,
 
#(c)
print '\n'+'*'*5+'题目(c)'+'*'*5
print '用整数2对其取余数，余数为0则偶数，否则奇数'
 
 
#(d)
print '\n'+'*'*5+'题目(d)'+'*'*5
def get():
    global num_1
    global num_2
    num_1 = input('请输入整数1：')
    num_2 = input('请输入整数2：')
def div():
     
    if num_1 % num_2 == 0 :
        print '整数%d能被整数%d整除' % (num_1, num_2)
        return True
    else:
        print '整数%d不能被整数%d整除' % (num_1, num_2)
        return False
 
get()
print div()
