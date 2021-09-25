while True:
	m, f, r = map(int, input().split())
	# すべて'-1'だったら、終了する
	if m == -1 and f == -1 and r == -1:
		break

	# 中間・期末を受けたかどうか、そして何点だったか
	score = 0
	if m >= 0:
		score+=m
	else:
		print('F')
		continue
	if f >= 0:
		score+=f
	else:
		print('F')
		continue

	# 試験を受けた場合の、評価決定
	if score >= 80:
		print('A')
	elif score >= 65:
		print('B')
	elif score >= 50:
		print('C')
	elif score >= 30:
		if r >= 50:
			print('C')
		else:
			print('D')
	else:
		print('F')
