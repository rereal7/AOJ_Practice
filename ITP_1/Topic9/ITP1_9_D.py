s = input()
n = int(input())
for i in range(n):
	q = input().split()
	command = q[0]
	a = int(q[1])
	b = int(q[2])
	if command == 'replace':
		s = s[:a] + q[3] + s[b+1:]
	elif command == 'reverse':
		s = s[:a] + s[a:b+1][::-1] + s[b+1:]
	else:
		print(s[a:b+1])