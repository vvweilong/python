#! ~/usr/bin/env python
# coding=utf-8

class MyClass :
	# 注意这里的下划线 是两个在一起
	def __init__(self,name,age):
		self.name=name;
		self.age=age;


	def showName(self):
		print self.name;

	def showAge(self):
		print self.age;



m=MyClass("someBody",10);
m.showName();
m.showAge();