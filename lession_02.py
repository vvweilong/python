#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''
# 奖金计算问题   10 20 40 60 100 万
#          0~10 10%   10~20 7.5% 20~40 5%  40~60 3% 60~100 1.5% 100+ 1%
#  根据输入数值 计算奖金
# 计算 应先计算出在哪个档位 然后 只算 最高档位数值 其他可固定数值
# 这里记录了 计算好的满档奖金 计算时可直接相加即可
'''
sureList = (0, 1, 0.75, 1, 0.9, 0.6);
perlist = (0.1, 0.075, 0.05, 0.03, 0.015, 0.01);
gearList = (0, 10, 20, 40, 60, 100);

money = input("请输入年收入(万)");

var = 0.0;
# 判断 收入 所在档次
for index in range(len(gearList)-1, 0, -1):
    if money > gearList[index]:
        var = money - gearList[index];
        print "档位多出资金：",var;
        var = var * perlist[index];
        print "这部分奖金 比例为",perlist[index];
        print "这部分奖金为",var;

        for i in range(0, index+1, 1):
            var += sureList[i];
            print "累计之前档位的奖金",sureList[i];
        break;


print("总奖金:");
print var;
