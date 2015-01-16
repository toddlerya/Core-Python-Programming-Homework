#!/usr/bin/env python
#coding:utf-8
 
"""
5-13 转换。写一个函数把由小时和分钟表示的时间转换为只用分钟表示的时间
"""
 
def transfomate():
    global hour,minute
    row_time = raw_input('输入你要转换的时间(格式H:M-->  xx:yy)：')
    time_list = row_time.split(':')
    hour = time_list[0]
    minute = time_list[1]
    total = int(hour) * 60 + int(minute)
    return '转换为分钟---->' + str(total)
 
print transfomate()
