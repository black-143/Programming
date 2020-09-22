from math import factorial as f

'''A Krishnamurthy number is a number whose sum of the factorial of digits is equal to the number itself. '''
n = int(input())
temp = n
s = 0
while n>0:
	mod = n % 10
	s += f(mod)
	n = n//10

if s==temp:
	print('YES')
else:
	print('NO')