#!/usr/bin/python

version = 2.0

def my_add(a,b):
	''' This is for addition of two numbers/string '''
	return a + b

def my_sub(a,b):
	''' This is for substraction of two numbers '''
	if a > b:
		return a - b
	else:
		return b - a

def my_multi(a,b):
	''' This is for multiplication of two numbers '''
	return a * b

def my_div(a,b):
	''' This is for division of two numbers '''
	return a/b

# Main

if __name__ == '__main__':
	print "Launching the missile!!!"