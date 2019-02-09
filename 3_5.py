#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random

SIZE = 10
MIN_ITEM = -15
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_max = MIN_ITEM
min_max_index = -1


for i in range(SIZE):
	if (array[i] < 0 and array[i] > min_max):
		min_max = array[i]
		min_max_index = i

print('Element is not found' if min_max_index == -1 else f'Element is {min_max} index of the element is {min_max_index}')
