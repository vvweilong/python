#! ~/usr/bin/env python
# coding=utf-8



filename="writeText.txt";


# 注意这里的文件权限！~！~！
file=open("writeText.txt","a+");
#  追加向项目文件写入内容
file.write("this is the file write test0\n");
file.write("this is the file write test1\n");
file.write("this is the file write test2\n");
file.flush();

# 为了读取需要把文件指针设置在文件首
file.seek(0);

#  从文件读取内容
lines = file.readlines();
for i in range(0,len(lines),1):
	print lines[i];

file.close();
