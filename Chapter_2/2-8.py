#! /usr/bin/env python
#coding: utf-8 
 
'''
题目要求：循环和运算符，创建一个包含五个固定数值的列表或元组，输出他们的和。
然后修改你的代码为接受用户输入数值。分别使用while和for循环实现。
'''
 
#固定值输出列表数字和
#while循环实现
aList = [1,2,3,4,5]
i = 0
l_sum = 0
#print len(aList)
while i < len(aList):
    l_sum = l_sum + int(aList[i])
    i += 1
print l_sum
 
#for循环实现
a_for_list = [1,3,5,7,9]
for_sum = 0
for j in a_for_list:
    for_sum = for_sum + j
print for_sum
 
 
#接受用户输入值，实现列表值加和输出
#while循环实现
get_list = []
k = 0
swap = 0
get_sum = 0
while k < 5:
    swap = raw_input('请输一个整数')
    get_list.append(swap) 
    get_sum += int(get_list[k]) 
    k += 1
print "列表元素各项加和的结果是: ", get_sum
 
#for循环实现
new_list = []
new_swap = 0
new_sum = 0
for l in range(5):
    new_swap = raw_input('请输入一个整数：') 
    new_list.append(new_swap)
    new_sum += int(new_list[l])
print "列表各元素加和结果是：", new_sum
