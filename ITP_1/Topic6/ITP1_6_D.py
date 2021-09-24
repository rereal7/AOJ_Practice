n, m = map(int, input().split())
A = [0 for i in range(n)]
B = [0 for i in range(m)]
for i in range(n):
	A[i] = list(map(int, input().split()))
# print(A)
for i in range(m):
	B[i] = int(input())
# print(B)

for i in range(n):
	c = 0
	for j in range(m):
		c += A[i][j] * B[j]
	print(c)