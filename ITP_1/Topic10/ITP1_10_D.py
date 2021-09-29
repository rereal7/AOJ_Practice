n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

# p=1,p=2,p=3
p = 1
while p < 4:
	sum = 0
	for i in range(n):
		sum += (abs(X[i] - Y[i]))**p
	print(f'{sum**(1/p):.6f}')
	p += 1

# p = ∞
ans = 0.0
for i in range(n):
		ans = max(ans, abs(X[i] - Y[i]))
print(f'{ans:.6f}')