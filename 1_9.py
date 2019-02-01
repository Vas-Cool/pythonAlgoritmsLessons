print("Write three number")
a = float(input('Write first number: '))
b = float(input('Write second number: '))
c = float(input('Write third number: '))

if a > b:
    x = a
    a = b
    b = x
    
else:
    x = b

if c > b:
	print(f'Middle number is {b}')

else:
	if a < c:
		print(f'Middle number is {c}')
	else:
		print(f'Middle number is {a}')	