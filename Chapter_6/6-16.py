#!/usr/bin/env python
# coding:utf-8
 
# author: toddlerya
# date: Jan 15 2015
 
"""
6–16.矩阵.处理矩阵 M 和 N 的加和乘操作.
"""
 
 
def matrix_add(mat_1, mat_2):
    # 矩阵加法应满足两个矩阵的行数列数相同
    if len_m1 != len_m2:
        print "Error, two matrix must have the same dimension!"
        return
    elif len_n1 != len_n2:
        print "Error, two matrix must have the same dimension!"
        return
    else:
        res_matrix = []
        for m in range(len_m1):
            res_matrix.append([])
            for n in range(len_n1):
                res_matrix[m].append(mat_1[m][n] + mat_2[m][n])
        return res_matrix
 
 
def matrix_multiply(mat_1, mat_2):
    # 矩阵乘法不满足交换律；矩阵乘法满足结合律
    if len_n1 != len_m2:
        print "Error, the dimension of matrix is wrong!"
    else:
        res_matrix = []
        for m in range(len_m1):
            res_matrix.append([])
            for r in range(len_n1):
                res_matrix[m].append(0)
                for n in range(len_n2):
                    res_matrix[m][r] += mat_1[m][n] * mat_2[n][r]
        return res_matrix
 
 
def enter():
    global matrix_1, matrix_2, len_m1, len_n1, len_m2, len_n2
    matrix_1 = input("Please input the matrix M\n")
    matrix_2 = input("Please input another matrix N\n")
    len_m1 = len(matrix_1)
    len_n1 = len(matrix_1[0])
    len_m2 = len(matrix_2)
    len_n2 = len(matrix_2[0])
 
if __name__ == "__main__":
    while True:
        choice = raw_input("Matrix addition(A) or Matrix multiplication(B) (q to quit)\n").lower()
        if choice == "a":
            enter()
            print matrix_add(matrix_1, matrix_2)
        elif choice == "b":
            enter()
            print matrix_multiply(matrix_1, matrix_2)
        elif choice == 'q':
            break
        elif choice != "a" or "b" or "q":
            print "Please check your enter!"
