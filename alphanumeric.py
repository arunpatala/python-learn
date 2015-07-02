

def count(s):
	d = 0
	a = 0
	for x in s:
		if x.isdigit(): d+=1
		elif x.isalpha(): a+=1
		else: pass
	return (d,a)

print count(raw_input())
