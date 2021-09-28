s = input()
print(s.swapcase())

# 別解
s = input()
ans = ''
for i in range(len(s)):
	ch = s[i]
	if ch.islower():
		ch = ch.upper()
	elif ch.isupper():
		ch = ch.lower()
	ans+=ch
print(ans)
