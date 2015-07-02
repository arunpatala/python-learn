
M = 3
N = 5

twoD = []
for i in range(0,M):
	oneD = []
	for j in range(0,N):
		oneD.append(i*j)
	twoD.append(oneD)

print twoD
