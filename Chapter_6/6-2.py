#! /usr/bin/env python
# coding: utf-8
 
"""
6–2.
字符串标识符.修改例 6-1 的 idcheck.py 脚本,使之可以检测长度为一的标识符,并且
可以识别 Python 关键字,对后一个要求,你可以使用 keyword 模块(特别是 keyword.kelist)来帮你.
"""
 
import string
import keyword
 
alphas = string.letters + '_'
nums = string.digits
key_list = keyword.kwlist
 
print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be ai least 2 chars long.'
 
myInput = raw_input('Identifier to test?')
 
if len(myInput) >= 1:
    if myInput[0] not in alphas:
        print '''invalid : first symbol must be alphabetic'''
    elif myInput in key_list:
        print '''invalid: the input id is a Python's keyword''' 
    else:
        alphnums = alphas + nums
        for otherChar in myInput[1:]:
            if otherChar not in alphnums:
                print '''invalid: remaining symbols must be alphanumeric'''
                break
        else:
            print "okay as an identifier"
