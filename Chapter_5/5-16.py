#! /usr/bin/env python
# coding:utf-8
 
"""
5-16 家庭财务。给定一个初始金额和月开销数, 使用循环,确定剩下的金额和当月的支
出数, 包括最后的支出数。 Payment() 函数会用到初始金额和月额度, 输出结果应该类似下
面的格式(例子中的数字仅用于演示):
Enter opening balance:100.00
Enter monthly payment: 16.13
Amount Remaining
Pymt#       Paid        Balance
-----      -------   --------
0           $ 0.00     $100.00
1           $16.13      $ 83.87
2           $16.13      $ 67.74
3           $16.13      $ 51.61
4           $16.13      $ 35.48
5           $16.13      $ 19.35
6           $16.13      $ 3.22
7           $ 3.22     $ 0.00
"""

"""
还是没能完美解决格式控制问题。随着输入数据位数改变到一定程度，会发生对不齐的现象。
"""
 
def get_total_money():
    global opening_balance
    opening_balance = raw_input('please input your opening balance(number):')
    try:
        opening_balance = float(opening_balance)
    except:
        print 'Wrong!! please try again(just a number)'
        get_total_money()
    else:
        print 'Enter opening balance success!'
 
def get_payment():
    global monthly_payment
    monthly_payment = raw_input('please input your monthly payment(number):')
    try:
        monthly_payment = float(monthly_payment)
    except:
        print 'Wrong!! please try again(just a number)'
        get_payment()
    else:
        print 'Enter monthly payment success!'
 
def payment():
    get_total_money()
    get_payment()   
    print 'Pymt#  ' + ' '*4 + 'Paid   ' + ' '*4 + 'Balance'
    print '-------' + ' '*4 + '-------' + ' '*4 + '-------'
    print '0', ' '*8, '$%.2f' % (monthly_payment - monthly_payment), ' '*4, '$%.2f' % opening_balance
    id = int(opening_balance / monthly_payment) 
    list_id = []
    for id in range(id+1):
        list_id.append(id)
    balance = opening_balance - monthly_payment
    for i in list_id[1:]:
        print '%d' % i, ' '*8, '$%.2f' % monthly_payment, ' '*3, '$%.2f' % balance
        if balance > monthly_payment:
            balance = balance - monthly_payment
    print (id+1), ' '*(9-len(str(id+1))), '$%.2f' % balance, ' '*4, '$%.2f' % (balance - balance)

payment()
