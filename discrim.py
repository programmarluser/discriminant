import math
print('discriminant formula')
print('input a b c')
a = int(input('enter a = '))
b = int(input('enter b = '))
c = int(input('enter c = '))
D = (b**2) - 4*a*c
print('D = ',D)
if D < 0:
	print('discriminant cannot be calculate')
elif D >= 0:
	d = math.sqrt(D)
	print('d = ',d)
	x1 = (-b + d) / (2 * a)
	x2 = (-b-d)/(2*a)
	print('x1,x2 = ',x1,x2)