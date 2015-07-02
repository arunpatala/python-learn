
total = 0
while True:
	arr = raw_input().split(" ")
	if(len(arr)!=2): break
	op = arr[0]
	amt = int(arr[1])
	if(op=="D"): total+=amt
	elif(op=="W"): total-=amt
	else: pass

print total
