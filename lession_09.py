#!/usr/bin/env python
# coding=utf-8
import math


# python 的数字类型
# 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
# 长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
# 浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

# a = 1;
# b = 10L;
# c1 = 1.0;
# c2 = 9e-1;
# d = complex(1, 1);
# print "Int 类型", a;
# print "Long 类型", b;
# print "Float 类型", c1;
# print "Float 类型", c2;
# print "complex 类型", d;

# # python 数字类型转换
# int(x [,base ])         将x转换为一个整数
# long(x [,base ])        将x转换为一个长整数
# float(x )               将x转换到一个浮点数
# complex(real [,imag ])  创建一个复数
# str(x )                 将对象 x 转换为字符串
# repr(x )                将对象 x 转换为表达式字符串
# eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )               将序列 s 转换为一个元组
# list(s )                将序列 s 转换为一个列表
# chr(x )                 将一个整数转换为一个字符
# unichr(x )              将一个整数转换为Unicode字符
# ord(x )                 将一个字符转换为它的整数值
# hex(x )                 将一个整数转换为一个十六进制字符串
# oct(x )                 将一个整数转换为一个八进制字符串

var_int = 1;
var_float = 8e2;
var_long = 10000L;
var_str = "90";
var_char = '8';
var_complex = complex(1, 3);
var_list = [1, 2, 3];
var_tuple = (4, 5, 6);

# print "float 转为 Int", int(var_float);
# print "long 转为 Int", int(var_long);
# print "str 转为 Int", int(var_str);
# print "char 转为 Int", int(var_char);
# print "complex.real 转为 Int", int(var_complex.real);
# print "complex.imag 转为 Int", int(var_complex.imag);

# 只有整数类型才能进行 16进制字符串转换
print "long 转为 hex str", hex(var_long);
print "long 转为 oct str", oct(var_long);
# print "str 转为 str", hex(var_str);
# print "char 转为 str", hex(var_char);
# print "complex.real 转为 str", hex(var_complex.real);
# print "complex.imag 转为 str", hex(var_complex.imag);

# 元组与列表
print "列表转元组", list(var_tuple);
print "元组转列表", tuple(var_list);

# abs(x)	返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y)	如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y 运算后的值。
# round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)	返回数字x的平方根

var_abs = -9;
var_fabs = -9.0;
var_ceil1 = 2.1;
var_ceil2 = -2.1;
var_floor1 = 2.1;
var_floor2 = -2.1;
var_round1 = 2.5;
var_round2 = -2.5;

print "abs绝对值 整型", abs(var_abs);
print "ceil上入整数", math.ceil(var_ceil1);
print "ceil上入整数", math.ceil(var_ceil2);
print "fabs 绝对值 浮点", math.fabs(var_fabs);
print "floor 下舍整数", math.floor(var_floor1);
print "floor 下舍整数", math.floor(var_floor2);
print "round 四舍五入", round(var_round1);
print "round 四舍五入", round(var_round2);
