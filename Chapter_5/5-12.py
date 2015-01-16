#!/usr/bin/env python
#coding:utf-8
 
"""
5-12 系统限制。写一段脚本确认一下你的 Python 所能处理的整数,长整数,浮点数和复
数的范围。
"""
 
import sys
 
print '系统所能处理的整数范围'
print str(-sys.maxint-1) + '<--->' + str(sys.maxint) 
 
print 
 
print '\n系统所能处理的长整数范围'
print (sys.long_info)
print
 
print '\n系统所能处理的浮点数范围'
print (sys.float_info)
 
#复数的怎么就是没找到呢，help(sys) 也没看到有复数
