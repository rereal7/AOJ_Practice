import math
while True:
	n = int(input())
	if n == 0:
		break
	S = list(map(int, input().split()))
	ave = sum(S)/n
	sumS = 0
	for i in S:
		sumS += (ave - i)**2
	a = sumS/n
	print(f'{math.sqrt(a):.5f}')
