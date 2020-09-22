import math

'''A number N is a Sastry Number if N concatenated with N + 1 gives a perfect square. '''
n = 183
#183 + 184 = 183184 = 4282
b=int(str(n)+str(n+1))

c=math.sqrt(b)

if(c*c==b):
	print(True)
else:
	print(False)
