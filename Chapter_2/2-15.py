#!/usr/bin/env python
#coding: utf-8
 
"""
2–15. 元素排序
(a)让用户输入三个数值并将分别将它们保存到3个不同的变量中。不使用列表或排序算法,
自己写代码来对这三个数由小到大排序。(b)修改(a)的解决方案,使之从大到小排序
"""
 
 
num_1 = input("num_1:")
num_2 = input("num_2:")
num_3 = input("num_3:")
 
if num_1 < num_2:
    if num_1 < num_3:
        if num_2 < num_3:
            print "从小到大排序：", num_1, num_2, num_3
        else:
            print "从小到大排序：", num_1, num_3, num_2
    else:
        print "从小到大排序：", num_3, num_1, num_2
else:
    if num_2 < num_3:
        if num_1 < num_3:
            print "从小到大排序：",num_2, num_1, num_3
        else:
            print "从小到大排序：",num_2, num_3, num_1
    else:
        print "从小到大排序：",num_3, num_2, num_1
 
 
if num_1 > num_2:
    if num_1 > num_3:
        if num_2 > num_3:
            print "从大到小排序：", num_1, num_2, num_3
        else:
            print "从大到小排序：", num_1, num_3, num_2
    else:
        print "从大到小排序：", num_3, num_1, num_2
else:
    if num_2 > num_3:
        if num_1 > num_3:
            print "从大到小排序：",num_2, num_1, num_3
        else:
            print "从大到小排序：",num_2, num_3, num_1
    else:
        print "从大到小排序：",num_3, num_2, num_1
