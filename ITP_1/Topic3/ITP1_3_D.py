a, b, c = map(int, input().split())
ans = 0
while a <= b:
	if c % a == 0:
		ans += 1
	a += 1
print(ans)