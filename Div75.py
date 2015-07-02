
# [x for x in range(2000,3200) if (x%7==0 and x%5!=0)]
l = []
for x in range(2000,3200):
	if(x%7==0 and x%5!=0):
		l.append(x)

print l
