'''A number is called as a Jumping Number if all adjacent digits in it differ by 1.
The difference between ‘9’ and ‘0’ is not considered as 1.'''

def check(n):
	a=str(n)
	for i in range(len(a)-1):
		if(abs(int(a[i+1])-int(a[i]))!=1):
			return False
	return True

for i in range(105):
	if(check(i)):
		print(i,end=" ")
print("\n")