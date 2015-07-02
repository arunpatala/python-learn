import math
x = 0
y = 0

while True:
	s = raw_input()
	if(not s): break
	arr = s.split(" ")
	cmd = arr[0]
	dist = int(arr[1])
	if cmd=="UP": x+=dist
	elif cmd=="DOWN": x-=dist
	elif cmd=="LEFT": y-=dist
	elif cmd=="RIGHT": y+=dist
	else: pass


print int(round(math.sqrt(x**2+y**2)))

