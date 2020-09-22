import math
'''
A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5. First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….'''
n = 50113 
pow = 1 
a = 0


while n:
	pow = pow*5
	if(n&1):
		a += pow
	n >>= 1
print(a)