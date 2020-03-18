# -*- coding: utf-8 -*-

import sys

def main():
	x, y, z = map(int, input().split(" "))
	result = -1
	if x != 0 and y != 0 and x != y: 
		if z%(x-y) == 0 and z/(x-y) > 0 :
			result = (int) (2*z/(x-y))
		if (z-y)%(x-y) == 0 and (z-y)/(x-y) > 0 :
			result = (int) (2*(z-y)/(x-y) - 1)
	
		if z==x :
			result=1
			


	
	if x==y and y==z :
		result=1
	if z == 0:
		result=0
		
		


	# your code

	print (result)


if __name__ == '__main__':
	main()
