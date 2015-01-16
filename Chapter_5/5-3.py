#!/usr/bin/env python
#coding: utf-8
 
def get_score():       
    global score
    score = raw_input('Please input the score(1~100): ')
    while not score.isdigit():
        score = raw_input('not a number, please try again: ')
    score = int(score)
    return score
     
def grade_test(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score <= 89:
        return 'B'
    elif 70 <= score <= 79:
        return 'C'
    elif 60 <= score <= 69:
        return 'D'
    elif  0 <= score <= 59:
        return 'F'
    else:
        return 'please confirm  0<= score <= 100'
        get_score()   #这个怎么无法调用成功
 
get_score()
print grade_test(score)
