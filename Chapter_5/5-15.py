# ! /usr/bin/env python
# coding: utf-8

"""
引用知识：http://blog.csdn.net/iwm_next/article/details/7450424
"""
 
"""
5–15.
最大公约数和最小公倍数。请计算两个整数的最大公约数和最小公倍数。
"""
 
# 最大公约数(greatest common divisor)，辗转相除法
def gcd():
    global a_get, b_get, num_gcd
    print '输入两个整数来求最大公约数'
    a_get = input('请输入第一个整数：')
    b_get = input('请输入第二个整数：')
    a = a_get
    b = b_get
    c = a % b 
    while (c != 0) :
        a = b
        b = c 
        c = a % b
    num_gcd = b
    return '这两个整数的最大公约数为 ' + str(num_gcd)
 
 
# 最小公倍数(least common multiple),两整数的乘积 除以 最大公约数
def lcm():
    num_lcm = (a_get * b_get) / num_gcd
    return '这两个整数的最小公倍数为 ' + str(num_lcm)
 
 
 
             
print gcd()
print lcm()
