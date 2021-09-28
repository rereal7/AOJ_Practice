while True:
	x = int(input())
	if x == 0:
		break
	x = str(x)
	X = list(map(int, x))
	print(sum(X))