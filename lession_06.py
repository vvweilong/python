#!/usr/bin/env python
# coding=utf-8


'''
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：

'''


def fibAt(n):
    result = 0;
    if n < 2:
        return n;
    else:
        result = fibAt(n - 1) + fibAt(n - 2);
    return result;


# 输出 当使用 raw input 时  直接输入数字会造成无法区分 输入类型二报错
a = input("请输入目标位置：");
r = fibAt(a);
print "目标费波那西数列 值为";
print r;
