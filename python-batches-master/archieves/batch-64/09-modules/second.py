#!/usr/bin/python
import sys
sys.path.insert(0,'/home/khyaathi/Documents/tuxfux-hlp-notes/python-notes/batch-64/09-modules/extra')
import first as f

def my_add(a,b):
	''' addition of two floats '''
	a=float(a)
	b=float(b)
	return a + b

# main
if __name__ == '__main__':
	print "addition of two floats is {}".format(my_add(10,21))
	print "addition of two string is {}".format(f.my_add("linux","rocks"))