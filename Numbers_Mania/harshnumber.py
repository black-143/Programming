n=18
s=0

'''Harshad Number is an integer that is divisible by the sum of its digits.
For Example :-
The number 18 is a Harshad number in base 10, because the sum of the digits 1 and 8 is 9 (1 + 8 = 9), and 18 is divisible by 9 (since 18 % 9 = 0)'''

for i in str(n):
	s=s+int(i)
if(n%s==0):
	print(n," is a harshad number")
else:
	print(n, " is not harshad number")