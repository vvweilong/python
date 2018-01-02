#! ~/usr/bin/env python
# coding=utf-8

file=open("writeText.txt","r");

try:
	file.write("this si the test comment");
	pass
except IOError as e:
	print e;
finally:
	file.close();
	pass

