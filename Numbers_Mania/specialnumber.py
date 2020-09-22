'''Special numbers are whose digits factorial sum is equal to the number'''

def fact(n):
	if(n==1):
		return n
	else:
		return n*fact(n-1)

def special(n):
	s=0
	for i in str(n):
		s=s+fact(int(i))
	if(s==n):
		return "Ok"
	else:
		return "Not"
print(special(145))