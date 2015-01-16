#!/usr/bin/env python
# coding:utf-8
 
# author:toddler
# date:Jan 14 2015
 
"""
6–14.随机数.设计一个"石头,剪子,布"游戏,有时又叫"Rochambeau",你小时候可能玩过,下面
是规则.你和你的对手,在同一时间做出特定的手势,必须是下面一种手势:石头,剪子,布.胜利者从
下面的规则中产生,这个规则本身是个悖论.
(a) the paper covers the rock,
布包石头.
(b)石头砸剪子,
(c)剪子剪破布.在你的计算机版本中,用户输入她/他的选项,计算机找一个随机选项,然后由你
的程序来决定一个胜利者或者平手.注意:最好的算法是尽量少的使用 if 语句.
"""
 
from random import choice
 
 
def Rochambeau(idea):
    dict_choice = {'stone':'1','shear':'2','paper':'3'}
    dict_result = {'11':'draw','22':'draw','33':'draw','12':'win','13':'lose','21':'lose','23':'win','31':'win','32':'lose'}
    cpu_choice = choice(['stome','shear','paper'])
    print "cpu choice : %s" % cpu_choice
    return "the result is : %s" % dict_result[dict_choice[idea] + dict_choice[cpu_choice]]

     
if __name__ == "__main__":
    while True:
        idea = raw_input("Please input your idea: stone or shear or paper (e to exit)\n") 
        print "-----------------------------------------"
        print "your choice : %s" % idea
        if idea.lower().strip() == 'e':
            break
        elif (idea != 'stone') and (idea != 'shear') and (idea != 'paper'):
            print "Please check your input"
            continue
        print Rochambeau(idea)
