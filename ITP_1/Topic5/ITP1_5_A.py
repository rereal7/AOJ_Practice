i = 0
while i < 1000000000:
	h, w = map(int, input().split())
	if h == 0 and w == 0:
		break
	for i in range(h):
		for j in range(w):
			print('#', end='')
		print()
	print()
	i += 1
