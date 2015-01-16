#! /usr/bin/env python
#coding: utf-8
"""
带 文本菜 单 的程序 写一个 带 文本菜 单 的程序,菜 单项 如下(1)取五个数的和 (2) 取五个
数的平均 值 ....(X)退出。由用 户 做一个 选择 ,然后 执 行相 应 的功能。当用 户选择 退出 时 程序
结 束。 这 个 程序的有用之 处 在于用 户 在功能之 间 切 换 不需要一遍一遍的重新启 动 你 的脚本。
( 这
对 开 发 人 员测试 自己的程序也会大有用 处 )
"""
while True:
    usr_choice = raw_input("请输入你的选项:\n (1)计算五个数字的加和\n (2)计算五个数字的平均值\n (x)退出\n")
    #print usr_choice == 1,type(usr_choice),
    print "你的选择：(%s)" % usr_choice
    if usr_choice == 'x':
        print "退出程序"
        break
    elif int(usr_choice) == 1:
        new_list = []
        new_swap = 0
        new_sum = 0
        for l in range(5):
            new_swap = raw_input('请输入一个数：') 
            new_list.append(new_swap)
            new_sum += long(new_list[l])
        print "五个数加和结果是：", new_sum
    elif int(usr_choice) == 2:
        new_list = []
        new_swap = 0
        new_sum = 0
        for l in range(5):
            new_swap = raw_input('请输入一个数：') 
            new_list.append(new_swap)
            new_sum += long(new_list[l])
        avg = new_sum / len(new_list)
        print "五个输入数字的平均值是：", avg
