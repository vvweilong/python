#!/usr/bin/env python
# coding=utf-8
import os
# 文件操作  创建文件 
myfile=open("myfile.txt","wb");
myfile.write("this is a content test");

myfile.close();

# 复制文件
# print commands.getstatesoutput("cp myfile.txt");
os.system("cp myfile.txt myfile.zip");
# os.system("zip my.zip myfile.txt");
os.system("unzip my.zip");


# 删除文件
# os.remove(myfile.name);



