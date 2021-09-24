while True:
	h, w = map(int, input().split())
	if h == 0 and w == 0:
		break
	for i in range(h):
		if i == 0 or i == h-1:
			for j in range(w):
				print('#', end='')
			print()
		else:
			for j in range(w):
				if j == 0 or j == w-1:
					print('#', end='')
				else:
					print('.', end='')
			print()
	print()

# x = 0
# while x < 1000000000:
# 	h, w = map(int, input().split())
# 	if h == 0 and w == 0:
# 		break
# 	for i in range(h):
# 		for j in range(w):
# 			if i == 0 or i == h-1 or j == 0 or j == w-1:
# 				print('#', end='')
# 			else:
# 				print('.', end='')
# 			print()
# 	print()
# 	x += 1
