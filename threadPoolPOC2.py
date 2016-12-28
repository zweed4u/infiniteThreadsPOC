#!/usr/bin/python

#Local library imports
import multiprocessing

def infiniteLoopTest(number):
	while 1:
		print number

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=len(range(5)))
    pool.map(infiniteLoopTest, range(5))