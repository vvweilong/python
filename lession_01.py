#!/usr/bin/env python
# coding=utf-8


# 循环输出 有 1234 组成的不重复3位数
# 只读列表
list = (1, 2, 3, 4);
i, j, k = 0, 0, 0;

# 百位数
for a in list :
    # 十位数
    for b in list:
        # 个位数
        for c in list:
            if (c != b) and (c != a) and (b != a):
                print (c+b*10+a*100)

