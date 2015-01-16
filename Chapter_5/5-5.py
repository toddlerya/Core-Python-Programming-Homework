#!/usr/bin/env python
#coding: utf-8
 
"""
5-5.取余。取一个任意小于 1 美元的金额,然后计算可以换成最少多少枚硬币。硬币有 1
美分,5美分,10 美分,25 美分四种。1 美元等于 100 美分。举例来说,0.76 美元换算结果
应该是3 枚 25 美分,1 枚 1 美分。类似 76 枚 1 美分,2 枚 25 美分+2 枚 10 美分+1 枚 5 美分+1
枚1 美分这样的结果都是不符合要求的。
"""
 
def dollar_slice(money):
    money = money * 100
    if 0 < money < 100:
        cent_25 = money // 25
        cent_10 = money % 25 //10
        cent_5  = money % 25 % 10 // 5
        cent_1  = money % 25 % 10 % 5
        print ('money can slice %d-25cent, %d-10cent, %d-5cent, %d-1cent') % (cent_25, cent_10, cent_5, cent_1)
    else:
        print 'Are you kiding me?'
 
money = raw_input('please input a money(0.0~1): ')
dollar_slice(float(money))
