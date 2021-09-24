a, b, c = map(int, input().split())
ans = 'No'
if a<b and b<c:
	ans = 'Yes'
print(ans)