W, H, x, y, r = map(int, input().split())
ans = 'Yes'
if x<0 or y<0:
	ans = 'No'
elif W-(x+r) < 0:
	ans = 'No'
elif H-(y+r) < 0:
	ans = 'No'
print(ans)