a = float(input('Write a year, please: '))

if (a % 4) == 0:
	if (a % 400) == 0:
		print('Year is leap-year')
	else:
		if (a % 100) == 0:
			print('Year is not leap-year')
		else:
			print('Year is leap-year')

else:
	print('Year is not leap-year')