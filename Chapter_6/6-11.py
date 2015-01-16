#!/usr/bin/env python
# coding: utf-8
 
"""
6–11.转换
(a)创建一个从整数到 IP 地址的转换程序,如下格式: WWW.XXX.YYY.ZZZ.
(b)更新你的程序,使之可以逆转换.
"""
 
#(a)
print '--------------(a)--------------'
def format_ip():
    num = raw_input('Enter ip number(12 integer)')
    w = num[0:3]
    x = num[3:6]
    y = num[6:9]
    z = num[9:12]
    tmp = [w,x,y,z]
    ip = '.'.join(tmp)
    return ip
 
if __name__ == '__main__':
    print format_ip()
     
 
#(b)
print '--------------(b)--------------'
def re_format_ip():
    ip = raw_input('Enter ip:')
    tmp = ip.split('.')
    num = ''.join(tmp) 
    return num
if __name__ == '__main__':
    print re_format_ip()
