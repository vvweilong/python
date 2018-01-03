#! ~/usr/bin/env python
# conding=utf-8 


# threading
import threading
import time

lock=threading.Lock();

count =0;

class MyThread(threading.Thread):
	
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self);
	def run(self):
		global count

		
		
		for x in xrange(1,5):
			time.sleep(2);	
			lock.acquire();
			count = count +1;
			print "Starting " , self.name;
			print "Starting count " ,count;
			lock.release();
try:
	thread1 = MyThread(1, "Thread-1", 1);
	thread2 = MyThread(2, "Thread-2", 2);

	thread1.start();
	thread2.start();
except Exception as e:
	raise e;

thread1.join();
thread2.join();

