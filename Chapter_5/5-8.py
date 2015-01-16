#!/usr/bin/env python
#coding:utf-8
 
"""
5-8 几何。计算面积和体积:
(a) 正方形 和 立方体
(b) 圆 和 球
"""
 
import types
import math
 
 
def area():
    choice = raw_input('请选择你要计算的几何体(1-正方形，2-立方体，3-圆，4-球),请输入你的选择(序号): ')
    if choice == '1':
        print '*'*10
        print '你要计算正方形的面积'
        print '*'*10
        length_of_the_side = raw_input('请输入正方形边长: ')
        square_area = eval(length_of_the_side) ** 2
        return '所求正方形的面积---->' + str(square_area)
         
    if choice == '2':
        print '*'*10
        print '你要计算立方体的面积'
        print '*'*10
        cube_side = raw_input('请输入立方体的边长:')
        cube_area = eval(cube_side) ** 2 * 6
        return '所求立方体的面积---->' + str(cube_area)
     
    if choice == '3':
        print '*'*10
        print '你要计算圆的面积'
        print '*'*10
        roundness_radius = raw_input('请输入圆的半径:') 
        roundness_area = eval(roundness_radius) ** 2 * math.pi
        return '所求圆形的面积----->' + str(roundness_area)    
     
    if choice == '4':
        print '*'*10
        print '你要计算球体的面积'
        print '*'*10
        sphere_radius = raw_input('请输入球体的半径:')
        sphere_area = eval(sphere_radius) * math.pi * 4
        return '所求球体的面积----->' + str(sphere_area)
 
def volume():
    choice = raw_input('请选择你要计算的几何体(1-立方体，2-球),请输入你的选择(序号): ')
        
    if choice == '1':
        print '*'*10
        print '你要计算立方体的体积'
        print '*'*10
        cube_side = raw_input('请输入立方体的边长:')
        cube_volume = eval(cube_side) ** 3
        return '所求立方体的体积---->' + str(cube_volume)
     
    if choice == '2':
        print '*'*10
        print '你要计算球体的体积'
        print '*'*10
        sphere_radius = raw_input('请输入球体的半径:')
        sphere_volume = eval(sphere_radius) ** 2 * math.pi * 4/3
        return '所求球体的体积----->' + str(sphere_volume)
 
 
def main():
    choice_main = raw_input('请选择要计算面积还是体积，输入序号(1-面积,2-体积):')
    if choice_main == '1':
        print area()
    elif choice_main == '2':
        print volume()
    else:
        print '请输入正确的选择序号'
        main()
         
main()
