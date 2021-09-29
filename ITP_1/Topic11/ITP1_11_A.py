Dice = input().split()
direction = input()

H = [Dice[3], Dice[0], Dice[2], Dice[5]]
W = [Dice[4], Dice[0], Dice[1], Dice[5]]

for i in direction:
	if i == 'E':
		tmp = [H[3]]
		H = tmp+H[:3]
		W[1] = H[1]
		W[3] = H[3]
	elif i == 'W':
		tmp = [H[0]]
		H = H[1:]+tmp
		W[1] = H[1]
		W[3] = H[3]
	elif i == 'S':
		tmp = [W[3]]
		W = tmp+W[:3]
		H[1] = W[1]
		H[3] = W[3]
	else:
		tmp = [W[0]]
		W = W[1:]+tmp
		H[1] = W[1]
		H[3] = W[3]
print(H[1])