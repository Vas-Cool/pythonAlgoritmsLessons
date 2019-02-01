#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
import sys

def show_size(x):
	mem = sys.getsizeof(x)
	if hasattr(x, '__iter__'):
		if not isinstance(x, str):
			for item in x:
				mem += show_size(item)
				sys.getsizeof(show_size(item))
	return mem

count_mem = 0

SIZE = 10
count_mem += show_size(SIZE)
print(f'Used memory is {count_mem}')
MIN_ITEM = -15
count_mem += show_size(MIN_ITEM)
print(f'Used memory is {count_mem}')
MAX_ITEM = 100
count_mem += show_size(MAX_ITEM)
print(f'Used memory is {count_mem}')
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
count_mem += show_size(array)
print(f'Used memory is {count_mem}')

min_max = MIN_ITEM
count_mem += show_size(min_max)
print(f'Used memory is {count_mem}')
min_max_index = -1
count_mem += show_size(min_max_index)
print(f'Used memory is {count_mem}')

for i in range(SIZE):
	if i == SIZE - 1:
		count_mem += show_size(i)
		print(f'Used memory is {count_mem}')
	if (array[i] < 0 and array[i] > min_max):
		min_max = array[i]
		min_max_index = i

print('Element is not found' if min_max_index == -1 else f'Element is {min_max} index of the element is {min_max_index}')
print(f'Used memory is {count_mem}')
# переменных 7 штук, памяти требуется больше (324)
# python 3.7.2 32-bit