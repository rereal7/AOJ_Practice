import math

def S(a, b, C):
	sinC = math.sin(math.radians(C))
	s = a * b * sinC/2
	return s

def c(a, b, C):
	cosC = math.cos(math.radians(C))
	c = math.sqrt(a**2 + b**2 -(2*a*b*cosC))
	return c

a, b, C = map(float, input().split())

s = S(a, b, C)
L = c(a, b, C) + a + b
h = s * 2 / a
print(f'{s:.4f}')
print(f'{L:.4f}')
print(f'{h:.4f}')