#!/usr/bin/env python
#coding: utf-8
 
'''
5-4.取余。判断给定年份是否是闰年。使用下面的公式:
    一个闰年就是指它可以被4整除,但不能被100整除,或者它既可以被4又可以被100整
除。比如1992,1996和2000年是闰年,但1967和1900则不是闰年。下一个是闰年的整世
纪是2400年
'''

# 题目第二个条件有错误，应该是被400整除，否则1900,1700这种年份都会被判断为闰年

 
def leapyear():
    year = raw_input("Please input a year: ")
    year = int(year)
         
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        return 'The %d is a bissextile ~ ' % year
    else:
        return 'The %d is not a bissextile ~' % year
     
print leapyear()
