#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.
count = [0] * (10 - 2)

for i in range(2, 100):
	for j in range(2, 10):
		if i % j == 0:
			count[j - 2] += 1
	
for i in range(2,10):
	print(f'Number of elements multiple of {i} is {count[i - 2]}')
