print("Write three sides of triangle")
a = float(input('Write first side: '))
b = float(input('Write second side: '))
c = float(input('Write second side: '))

if a > b:
    x = a
    a = b
    b = x
    
else:
    x = b

if c > b:
	x = x

else:
	x = c
	c = b
	b = x

if c <= a + b:
	x = 0
	if c == b:
		x = x + 1
	if a == b:
		x = x + 1
else:
	x = -1


if x == -1:
	print('Triangle is not possible')
if x == 0:
	print('Triangle is scalene')
if x == 1:
	print('Triangle is isosceles')
if x == 2:
	print('Triangle is regular')