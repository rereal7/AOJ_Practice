i = 0
while i < 3000:
	x, y = map(int, input().split())
	if x == 0 and y == 0:
		break
	if x > y:
		tmp = x
		x = y
		y = tmp
	print(f'{x} {y}')
	i += 1
