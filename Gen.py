

def gen(n):
	for i in range(0,n):
		if (i%7==0 and i%5!=0):
			yield i

for i in gen(1000):
	print i
