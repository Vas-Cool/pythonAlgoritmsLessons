#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_ = MAX_ITEM
max_ = MIN_ITEM

min_index = 0 
max_index = 0

for i in range(SIZE):
	if array[i] < min_:
		min_ = array[i]
		min_index = i
	if array[i] > max_:
		max_ = array[i]
		max_index = i

print(min_, max_)


x = array[min_index]
array[min_index] = array[max_index]
array[max_index] = x
print(array)