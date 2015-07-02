
M = 3
N = 5

twoD = [[0 for y in range(N)] for x in range(M)]
for i in range(0,M):
	for j in range(0,N):
		twoD[i][j] = i*j

print twoD
