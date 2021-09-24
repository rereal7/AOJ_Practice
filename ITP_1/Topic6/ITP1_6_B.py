n = int(input())
pattern = ["S", "H", "C", "D"]
cards = [[False for i in range(13)] for j in range(4)]
for i in range(n):
	p, r = input().split()
	r = int(r)
	cards[pattern.index(p)][r-1] = True

# for a in range(4):
# 	for b in range(13):
# 		if cards[a][b] == False:
# 			print(pattern[a], b+1)
# 		# if b == False:
# 		# 	print(pattern[a], b+1)

# 別解
for i, a in enumerate(cards):
	for j, b in enumerate(a):
		if cards[i][j] == False:
			print(pattern[i], j+1)

# enumerate()のデモ
# l = ['Alice', 'Bob', 'Charlie']

# for i, name in enumerate(l):
#     print(i, name)
# # 0 Alice
# # 1 Bob
# # 2 Charlie