"""
6–1.

字符串.string 模块中是否有一种字符串方法或者函数可以帮我鉴定一下一个字符串

是否是另一个大字符串的一部分?
"""


# 1
str_1 = 'perfect is shit'
if 'shit' in str_1:
    print 'INININ!!!'
else:
    print 'Not ININININ!!!'
 
# 2
str_1.find('shit')
str_1.count('shit')
str_1.index('shit')
