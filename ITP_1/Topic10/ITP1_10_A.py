import math

def get_distance(x1, y1, x2, y2):
	d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
	return d

x1, y1, x2, y2 = map(float, input().split()) 

d = get_distance(x1, y1, x2, y2)
print(d)