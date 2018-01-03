#! ~/usr/bin/env python
# conding=utf-8 


import thread
import time


def printm(name):
	for i in range(0,5,1):
		time.sleep(1);
		print "-----",i;	

	


try:
	for j in range(0,5,1):
		thread.start_new_thread(printm,("abc",));	
except Exception as e:
	raise e;


