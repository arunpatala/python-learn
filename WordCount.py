

def count(words):
	d = dict()
	for w in words:
		d[w] = d.get(w,0) + 1
	return d

print count(raw_input().split(" "))
