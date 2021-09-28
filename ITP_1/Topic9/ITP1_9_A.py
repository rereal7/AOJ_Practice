w = input()
ans = 0
while True:
	A = input()
	if A == 'END_OF_TEXT':
		break
	ans += A.lower().split().count(w)
print(ans)