#!/usr/bin/env python
# coding:utf-8
 
"""
6–12.字符串
(a)创建一个名字为 findchr()的函数,函数声明如下:
def findchr(string, char)
findchr()要在字符串 string 中查找字符 char,找到就返回该值的索引,否则返回-1.不能用
string.*find()或者 string.*index()函数和方法
(b)创建另一个叫 rfindchr()的函数,查找字符 char 最后一次出现的位置.它跟 findchr()工作
类似,不过它是从字符串的最后开始向前查找的.
(c)创建第三个函数,名字叫 subchr(),声明如下:
def subchr(string, origchar, newchar)
subchr()跟 findchr()类似,不同的是,如果找到匹配的字符就用新的字符替换原先字符.返回
修改后的字符串.
"""
 
import types
 
 
#(a)
def findchr(string, char):
    print 'The string is "%s" and the char is "%s"' % (string, char)
    result = []
    for i, j in enumerate(string):
        if char == j:
            result.append(i)         
    if len(result) != 0:
        print 'the index of char:'
        return result
    else:
        return -1

     
#(b)
def rfindchr(string, char):
    print 'The string is "%s" and the char is "%s"' % (string, char)
    l = len(string)
    for i, j in enumerate(string[::-1]):
        if char == j:
            result = l-i
            break
    if type(result) is types.IntType :
        print 'the last index of char:'
        return result
    else:
        return -1
 
 
#(c)
def subchr(string, origchar, newchar):
    print 'The string is "%s" ,the origchar is "%s" and the char is "%s"' % (string, origchar,newchar)
    result = []
    str_list = list(string)
    for i, j in enumerate(str_list):
        if origchar == j:
            str_list[i] = newchar
    result = ''.join(str_list)
    return result
 
print '----(a)-----'
print findchr('dota is the best','i')
print '----(b)-----'
print rfindchr('dota is the best!','t')
print '----(c)-----'
print subchr('I love dota','I','We')
