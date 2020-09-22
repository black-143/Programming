a=[2,2,3,4]
a.sort()
m=-1
for i in a:
	if(a.count(i)==i):
		m=i
print(m)