alp = [chr(i) for i in range(97, 97+26)]
s = ''
while True:
	try:
		s += input().lower()
	except EOFError:
		break

for i in range(26):
	print(f'{alp[i]} : {s.count(alp[i])}')