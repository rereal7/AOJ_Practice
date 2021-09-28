n, m, l = map(int, input().split())

A = []
for i in range(n):
	x = list(map(int, input().split()))
	A.append(x)
B = []
for i in range(m):
	y = list(map(int, input().split()))
	B.append(y)

C = []
for i in range(n):
	y = []
	for j in range(l):
		sum = 0
		for k in range(m):
			sum += A[i][k] * B[k][j]
		y.append(sum)
	print(' '.join(map(str, y)))