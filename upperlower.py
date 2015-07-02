

def count(s):
	d = 0
	a = 0
	for x in s:
		if x.isupper(): d+=1
		elif x.islower(): a+=1
		else: pass
	return (d,a)

print count(raw_input())
