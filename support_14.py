#! ~/usr/bin/env python
# coding=utf-8


#父类 
class Parent:
	def __init__(self,name):
		self.name=name;
	def show(self):
		print "my name is :",self.name;



class Child(Parent):
	def tell(self):
		print "my name is ",self.name;