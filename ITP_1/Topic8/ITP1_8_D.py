s = input()
p = input()

s += s
if s.find(p) >= 0:
	print('Yes')
else:
	print('No')


# 別解
s = input()
p = input()

ans = 'No'
for i in range(len(s)):
	if s.find(p) >= 0:
		ans = 'Yes'
		break
	else:
		s = s[1:]+s[0]
print(ans)