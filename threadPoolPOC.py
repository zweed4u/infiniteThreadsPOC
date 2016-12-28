#!/usr/bin/python
#POC - thread pool infinite loops - shared resources see here:
#https://www.codementor.io/python/tutorial/simple-parallelism-in-python

#Local library imports
import time
from multiprocessing.dummy import Pool as ThreadPool

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
	iterable={
		'number':[0,1,2,3,4,5,6,7,8,9]

	}
	pool = ThreadPool(len(iterable['number']))
	pool.map(func=infiniteLoopTest,iterable=iterable['number'])