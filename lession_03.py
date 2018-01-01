#!/usr/bin/env python
# -*- coding=UTF-8 -*-


# 判断一个数 是不是平方数 并找出 底数
def isSquareNum(num):
    for i in range(1, num / 2, 1):
        if i * i == num:
            return i;
    return 0;

'''
一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

如何判断完全平方数？手工判断。。。
'''
# 未知数x
x = 0

# 首先找出平方数 a 和平方数 b
a = 100;
b = 268;

for x in range(1, 100, 1):
    # 判断+100 是不是平方数
    if isSquareNum(x + 100) != 0:
        print "+100 为平方数 ",x;
        if isSquareNum(x+268)!=0:
            print "求解这个数为 ",x;

print "在当前范围没找到符合条件的值";





