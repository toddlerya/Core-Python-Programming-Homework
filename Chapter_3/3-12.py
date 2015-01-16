#! /usr/bin/env python
#coding: utf-8
 
"""
easy_text.py-----write and read text
合并源文件。将两段程序合并成一个,给它起一个你喜欢的名字,比方
readNwriteTextFiles.py。让用户自己选择是创建还是显示一个文本文件
"""

 
import sys
import os
ls = os.linesep
#tips:
#os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
 
def write_text():
        #get filename
    while True:
        fname = raw_input('input your filename:')
        if os.path.exists(fname):
            print "error: '%s' already exists " % fname
            continue
        else:
            break
 
    #get file content (text) lines
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
         
    #loop until user terminates input
    while True:
        entry = raw_input(' T_T > ')
        if entry == '.':
            break
        else:
            all.append(entry)
 
    #write line to file with proper line-ending
    fobj = open(fname, 'w')
    fobj.writelines( ['%s%s' % (x, ls) for x in all] )
    fobj.close()
    print 'DONE!' 
     
def read_text():
    #get filename
    fname = raw_input('Enter filename: ')
    print
 
    #attempt to open file for reading
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error:", e
    else:
        #display contents to the screen
        for eachLine in fobj:
            # strip() 删除字符串开头或末尾的指定字符，不加参数，默认删除空格
            eachLine = eachLine.strip()
            print eachLine
        fobj.close()
 
choice = ''
     
while choice != "q":
    choice = raw_input("Please choose write(w) or read(r) or quit(q):\n")
    if choice == 'w':
        write_text()
    elif choice == 'r':
        read_text()
    else:
        sys.exit()
