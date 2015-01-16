#! /usr/bin/env python
# coding: utf-8
 
"""
6–8.
列表.给出一个整数值,返回代表该值的英文,比如输入 89 返回"eight-nine"。附加题:
能够返回符合英文语法规则的形式,比如输入“89”返回“eighty-nine”。本练习中的值限定在家 0
到 1,000.
"""
 
# 这道题用字典肯定好做！！！！
 
def get():
    global get_num
    get_num = raw_input('please input your number:')
    try:
        get_num = int(get_num)
    except:
        print 'Error Input,please input a number!'
        get() 
    else:
        print 'Input success!'
#(1)
eng_list = []
eng = "zero,one,two,three,four,five,six,seven,eight,nine,ten"
eng_list = eng.split(',')
result = []
get()
get_list = list(str(get_num))
for i in get_list:
    result.append(eng_list[int(i)])
 
print '-'.join(result)
 
#(2)
print '------------------附加题-------------------'
'分三组，(1)0-9的数字做一个列表，(2)10-19的数字做一个列表，(3)20、30、40……做一个列表'
str_1 = "zero,one,two,three,four,five,six,seven,eight,nine"
str_2 = "ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty"
str_3 = "thirty,forty,fifty,sixty,seventy,eighty,ninety"
eng_1 = [] 
eng_2 = []
eng_3 = []
eng_1 = str_1.split(',')
eng_2 = str_2.split(',')
eng_3 = str_3.split(',')
 
#调用get() 
get()
 
#把输入的数字按“千，百，十，个”位，分割  
kilo = get_num / 1000
hund = get_num % 1000 / 100
deca = get_num % 1000 % 100 / 10
unit = get_num % 1000 % 100 %10 
 
'--------------------------------------------------------------------' 
#写完才发现，其实用格式化输出更好，连接字符串的方式不太好。
#print '%d thousand- %d hundred' % (eng_1[int(kilo)], eng_1[int(hund)]
'--------------------------------------------------------------------' 
   
if kilo != 0:
    if hund != 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_2[int(unit)]
        elif int(deca)==0 and unit != 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred','-',eng_1[int(unit)]
        elif int(deca)==0 and unit == 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(hund)],'hundred'
    elif hund == 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_1[int(kilo)],'thousand','-',eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_1[int(kilo)],'thousand','-',eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_1[int(kilo)],'thousand','-',eng_2[int(unit)]
        elif int(deca)==0 and unit != 0:
            print eng_1[int(kilo)],'thousand','-',eng_1[int(unit)]
        elif int(deca)==0 and unit == 0:
            print eng_1[int(kilo)],'thousand',
elif kilo == 0:
    if hund != 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_1[int(hund)],'hundred','-',eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_1[int(hund)],'hundred','-',eng_2[int(unit)]
        elif int(deca)==0 and unit != 0:
            print eng_1[int(hund)],'hundred','-',eng_1[int(unit)]
        elif int(deca)==0 and unit == 0:
            print eng_1[int(hund)],'hundred'
    elif hund == 0 :
        if int(deca) >= 2 and unit !=0:
            print eng_3[int(deca)-3],'-',eng_1[int(unit)]
        elif int(deca) >= 2 and unit == 0:
            print eng_3[int(deca)-3]
        elif 1<=int(deca)<2:
            print eng_2[int(unit)]
        elif int(deca)==0:
            print eng_1[int(unit)]
