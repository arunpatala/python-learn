import math
l = []
C = 50
H = 30
def CDH(D) : return math.sqrt(2*C*D/H)

for x in raw_input().split(","):
	l.append(str(int(CDH(float(x)))))

print ",".join(l)
