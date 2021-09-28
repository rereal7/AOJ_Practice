while True:
	n = input()
	if n == '-':
		break
	m = int(input())
	for i in range(m):
		h = int(input())
		n = n[h:] + n[0:h]
	print(n)