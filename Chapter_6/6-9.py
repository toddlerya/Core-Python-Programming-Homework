#! /usr/bin/env python
# coding: utf-8
 
"""
6–9.
转换.为练习 5-13 写一个姊妹函数, 接受分钟数, 返回小时数和分钟数. 总时间不
变,并且要求小时数尽可能大.
"""

#5-13.py
'''
def transfomate():
    global hour,minute
    row_time = raw_input('输入你要转换的时间(格式H:M-->  xx:yy)：')
    time_list = row_time.split(':')
    hour = time_list[0]
    minute = time_list[1]
    total = int(hour) * 60 + int(minute)
    return '转换为分钟---->' + str(total)
 
print transfomate()
'''    
     
def m_trans_h():
    get_time = int(raw_input('输入你要转换的时间(分钟数-->一个正整数):'))
    hour = get_time / 60
    minute = get_time % 60 
    print hour,'H',':',minute,'M'
     
m_trans_h()
