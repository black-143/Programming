n=135
visited=set()

'''If a number is happy, then all members of its sequence are happy; if a number is unhappy, all members of the sequence are unhappy.
For example, 19 is happy, as the associated sequence is:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1.'''

while n!=0 and not n in visited:
	visited.add(n)
	n=sum(map(lambda x:int(x)**2,str(n)))
	print(visited)
	print(n)
print(not n in visited)