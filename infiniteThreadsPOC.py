#!/usr/bin/python
#POC - multiple threaded infinite loops - non shared resources see here:
#http://stackoverflow.com/questions/23100704/running-infinite-loops-using-threads-in-python

#Local library imports
import time, threading

def infiniteLoopTest(num):
	"""
	Infinite loop that prints passed parameter
	:params num: integer - passed from the main 
	"""
	while 1:
		print num
		print
		time.sleep(1)

if __name__ == '__main__':
	"""
	Main slots controller
	"""
	for number in range(10):
		t = threading.Thread(target=infiniteLoopTest, args=(number,))
		t.start()