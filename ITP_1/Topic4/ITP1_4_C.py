i = 0
while i < 100000000:
	a, op, b = input().split()
	a = int(a)
	b = int(b)
	if op == '+':
		ans = a+b
	elif op == '-':
		ans = a-b
	elif op == '*':
		ans = a*b
	elif op == '/':
		ans = a//b
	else:
		break
	i += 1
	print(ans)