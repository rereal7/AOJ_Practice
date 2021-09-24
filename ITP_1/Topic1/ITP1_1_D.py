s = int(input())

h = s//3600
s -= 3600*h
m = s//60
s -= 60*m

print(str(h) + ':' + str(m) + ':' + str(s))

# 模範解答
# s = int(input())
# h = s // 3600
# m = s % 3600 // 60
# s = s % 60
# print(f"{h}:{m}:{s}")