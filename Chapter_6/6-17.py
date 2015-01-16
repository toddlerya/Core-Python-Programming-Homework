#!/usr/bin/env python
# coding:utf-8

"""
6–17.方法.实现一个叫 myPop()的函数,功能类似于列表的 pop()方法,用一个列表作为输入,
移除列表的最新一个元素,并返回它.
"""


def myPop(alist):
    new_list = alist[:-1]
    return new_list


if __name__ == "__main__":
    get_list = input("Please input your list: \n")
    print "The initializing list is %s" % get_list
    print "The new list is", myPop(get_list)
