#В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = -15
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_1 = MAX_ITEM
min_2 = MAX_ITEM
game_open = 0

if (array[0] < min_1):
	min_1 = array[0]
	min_2 = array[0]

for i in range(1, SIZE):
	if (array[i] < min_1):
		min_2 = min_1
		min_1 = array[i]
	elif (min_1 < array[i] and array[i] < min_2):
		min_2 = array[i]

print(min_1, min_2)