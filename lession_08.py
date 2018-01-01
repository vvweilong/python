#!/usr/bin/env python
# coding=utf-8

#
# 条件语句
# 循环语句与 java 用法几乎一样

# if
while (True):
    var = input("请输入数值(输入-1 结束程序)：");
    if var == -1:
        print "if 输入的是%d" % var;
        break
    elif var == 0:
        print "elif 输入的是%d" % var;
    elif var == 1:
        print "elif 输入的是%d" % var;
    else:
        print "这里是 else";
