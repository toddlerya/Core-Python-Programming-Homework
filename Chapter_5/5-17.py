#!/usr/bin/env python
# coding:utf-8
 
"""
5-17 随机数。熟读随机数模块然后解下面的题:
生成一个有 N 个元素的由随机数 n 组成的列表, 其中 N 和 n 的取值范围分别为: (1 <
N <= 100), (0 <= n <= 231 -1)。然后再随机从这个列表中取 N (1 <= N <= 100)个随机数
出来, 对它们排序,然后显示这个子集。
"""
 
import random
N_num = random.randrange(2, 101, 1) #生成N的基数， 1 < N <= 100 
random_list = []
for N in range(N_num):   #生成一个有N个元素的列表
    random_list.append(random.randrange(0,231,1))  #列表由 0 <= n <= 230 的数字组成
 
select_list = []
for n in range(random.randrange(1, N_num, 1)):  #从生成的列表中随机取出 1<=N<=100个随机数，不能超过列表的个数上限
    select_list.append(random.choice(random_list))
 
sort_list = []
sort_list = sorted(select_list)  #对其排序生成一个新的序列
 
print random_list
print 
print len(random_list)
print '-'*40
print select_list
print
print len(select_list)
print '-'*15
 
print sort_list
