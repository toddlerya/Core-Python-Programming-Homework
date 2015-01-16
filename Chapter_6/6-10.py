#!/usr/bin/env python
# coding:utf-8
 
"""
6–10.字符串.写一个函数,返回一个跟输入字符串相似的字符串,要求字符串的大小写反转.
比如,输入"Mr.Ed",应该返回"mR.eD"作为输出.
"""
 
str_1 = raw_input('Enter your string:')
str_list = list(str_1)
result_list = []
for i in str_list:
    if i.isupper():
        result_list.append(i.lower())
    elif i.islower():
        result_list.append(i.upper())
    else:
        result_list.append(i)
 
result = ''.join(result_list)
print 'Before: %s' % str_1
print 'After: %s' % result
