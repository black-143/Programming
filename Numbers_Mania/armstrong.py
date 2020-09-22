n=153
temp=n
Sum=0

'''An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself.
For example : 371 is an Armstrong number since 3*3*3 + 7*7*7 + 1*1*1 = 371. 
Another - 153 = 1*1*1 + 5*5*5 + 3*3*3'''
while(temp>0):
	dig=temp%10
	Sum+=dig**3
	temp//=10

if(Sum==n):
	print("Ok")
else:
	print("No")
