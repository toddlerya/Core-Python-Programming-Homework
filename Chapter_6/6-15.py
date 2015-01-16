#!/usr/bin/env python
# coding:utf-8
 
# date: Jan 15 2015
# author: toddlerya
 
"""
6–15.转换
(a)给出两个可识别格式的日期,比如 MM/DD/YY 或者 DD/MM/YY 格式,计算出两个日期间的天
数.
(b)给出一个人的生日,计算从此人出生到现在的天数,包括所有的闰月.
(c)还是上面的例子,计算出到此人下次过生日还有多少天
"""
 
from datetime import date
 
 
def calcdate(string1, string2):
    temp_list1 = string1.split("/")
    temp_list2 = string2.split("/")
    days_count = ""
    first_date = date(int(temp_list1[2]), int(temp_list1[1]), int(temp_list1[0]))
    second_date = date(int(temp_list2[2]), int(temp_list2[1]), int(temp_list2[0]))
    if first_date < second_date:
        days_count = abs(second_date - first_date)
    return days_count.days
 
 
# 以一个人的生日为参数，计算从此人出生到现在的天数，包括所有的闰月
def calcbirth(string):
    today = date.today()
    time_to_birth = ""
    temp_list = string.split("/")
    birth = date(int(temp_list[2]), int(temp_list[1]), int(temp_list[0]))
    if birth < today:
        time_to_birth = abs(today - birth)
    else:
        print("Please input the right birth")
    return time_to_birth.days   # 返回计算后的天数，用".days"取得天数，舍去小数点
 
 
def nextbirth(string):
    today = date.today()
    time_to_birth = ""
    temp_list = string.split("/")
    month_day = date(today.year, int(temp_list[1]), int(temp_list[0]))
    birth = date(int(today.year+1), int(temp_list[1]), int(temp_list[0]))
    if today < month_day:
        next_time_to_birth = abs(month_day - today)
    elif today < birth:
        next_time_to_birth = abs(birth - today)
    else:
        print("Please input the right birth")
    return next_time_to_birth.days   # 返回计算后的天数，用".days"取得天数，舍去小数点
 
 
if __name__ == "__main__":
    while True:
        choice = raw_input("I can do something:\na: Count the number of days between two date\n"
                           "b: Count the number of days since you born\n"
                           "c: Count the number of days before your next birth\n"
                           "q to quit\n")
        if choice == 'q':
            break
        elif choice == 'a':
            str_1 = raw_input("Please enter your first date: like  DD/MM/YY \n")
            str_2 = raw_input("Please enter your second date\n")
            try:
                print("The number of days between two date is", calcdate(str_1, str_2))
            except:
                print("Please check your enter format DD/MM/YY")
        elif choice == 'b':
            str_date = raw_input("Please enter your date: like  DD/MM/YY \n")
            try:
                print "You had born", calcbirth(str_date), "days"
            except:
                print("Please check your enter format DD/MM/YY")
        elif choice == 'c':
            str_date = raw_input("Please enter your birth date: like  DD/MM/YY \n")
            try:
                print "There are", nextbirth(str_date), "days of your next birthdays"
            except:
                print("Please check your enter format DD/MM/YY")
