#! /usr/bin/env python
# coding: utf-8
 
'''
6–3.
排序
(a) 输入一串数字,从大到小排列之.
(b) 跟 a 一样,不过要用字典序从大到小排列之.
'''
#(a)
def get_num():
    global num_list
    num_list = []
    num = ''
    while num != '!':
        num = raw_input('输入一些数字，以"！"结束').strip()
        if num != '!':
            try:
                num = float(num)
            except:
                print '输入有误，请重新输入'
                get_num()
            else:
                num_list.append(num) 
        else:
            break
    return num_list
 
def sort_descending():
    get_num()
    print sorted(num_list, reverse = True)
 
print '----------------(a)----------------'
sort_descending()
 
#(b)
print '-----------------(b)---------------'
key_sort = []
while True:
    k = raw_input('输入一些数字吧，以字典序排列大小,以"#"结束输入：')
    if k != '#':
        key_sort.append(k)
    else:
        break
        
print sorted(key_sort, reverse = True)
