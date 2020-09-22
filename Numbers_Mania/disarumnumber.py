n = 135
temp = n
Sum = 0
pos = len(str(n))

'''A number will be called DISARIUM if sum of its digits powered with their respective position is equal to the original number.
For example 135 is a DISARIUM
(Workings 11+32+53 = 135, some other DISARIUM are 89, 175, 518 etc)'''

while temp > 0:
      digit = temp%10
      Sum += digit**pos
      temp //= 10
      pos -= 1
if(Sum==n):
	print("OK")
else:
	print("NO")
