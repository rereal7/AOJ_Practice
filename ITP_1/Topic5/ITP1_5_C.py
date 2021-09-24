while True:
	h, w = map(int, input().split())
	if h == 0 and w == 0:
		break
	for i in range(1, h+1):
		if i%2 == 1:                   #奇数行
			for j in range(1, w+1):
				if j%2 == 1:           #奇数列
					print('#', end='')
				else:
					print('.', end='')
			print()
		else:                           #偶数行
			for j in range(1, w+1):
				if j%2 == 0:            #偶数列
					print('#', end='')
				else:
					print('.', end='')
			print()
	print()

# 別解(こっちのがスマートでいい)
while True:
	h, w = map(int, input().split())
	if h == 0 and w == 0:
		break
	for i in range(h):
		for j in range(w):
			x = (i+j)%2            #
			if x == 0:             #偶数列
				print('#', end='')
			else:                  #奇数列
				print('.', end='')
		print()
	print()