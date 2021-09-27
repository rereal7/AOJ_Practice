R = []
r, c = map(int, input().split())
for i in range(r):
	A = list(map(int, input().split()))
	A.append(sum(A))
	R.append(A)

C = []
for i in range(c+1):
	add = 0
	for j in range(r):
		add += R[j][i]
	C.append(add)
R.append(C)

for i in R:
	print(" ".join(map(str, i)))