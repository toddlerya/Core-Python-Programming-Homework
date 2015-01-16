#!/usr/bin/env python
# coding: utf-8
 
"""
6–6.
字符串.创建一个 string.strip()的替代函数:接受一个字符串,去掉它前面和后面的
空格(如果使用 string.*strip()函数那本练习就没有意义了)
"""
 
 
def blank():
    get_str = raw_input('please in put your string: ')
    r = len(get_str) - 1    
    l = 0
    while get_str[l] == ' ':
        l = l + 1
    while get_str[r] == ' ':
        r = r - 1
    result = get_str[l:r+1]
    return result
 
 
if __name__ == '__main__':
    print blank()
