n = int(input())
t = 0
h = 0
for i in range(n):
	x, y = input().split()
	if x < y:
		h += 3
	elif x > y:
		t += 3
	else:
		t += 1
		h += 1
print(f'{t} {h}')
