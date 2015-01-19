#!/usr/bin/env python
# coding: utf-8
# author: toddlerya
# date: Jan 18 2015

"""
7–3.
字典和列表的方法。
(a) 创建一个字典,并把这个字典中的键按照字母顺序显示出来。
(b) 现在根据已按照字母顺序排序好的键,显示出这个字典中的键和值。
(c)同(b),但这次是根据已按照字母顺序排序好的字典的值,显示出这个字典中的键和值。(注
意:对字典和哈希表来说,这样做一般没有什么实际意义,因为大多数访问和排序(如果需要)都是
基于字典的键,这里只把它作为一个练习。)
"""

# (a) and (b)
print '-----------(a) and (b)-----------'
dict1 = {'a': 'w', 'c': 'v', 'e': 'y', 'b': 'x', 'd': 'z'}
for j in sorted(dict1):
    print "tht key is ", j, "and the value is ", dict1[j]

# (c)
print '----------------(c)--------------\n'
for value in sorted(dict1.values()):
    for key in dict1.keys():
        if dict1[key] == value:
            print "The key is", key, "The value is", value
