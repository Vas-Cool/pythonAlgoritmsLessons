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
MIN_ITEM = -800
count_mem += show_size(MIN_ITEM)
print(f'Used memory is {count_mem}')
MAX_ITEM = -750
count_mem += show_size(MAX_ITEM)
print(f'Used memory is {count_mem}')
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
count_mem += show_size(array)
print(f'Used memory is {count_mem}')
print(array)

# вариант 1
i = 0
count_mem += show_size(i)
print(f'Used memory is {count_mem}')
index = -1
count_mem += show_size(index)
print(f'Used memory is {count_mem}')
while i < len(array):   # или for i in range(len(array)):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

if index != -1:
    print(f'Максимальное отрицательное число {array[index]} '
          f'находится в ячейке {index}')

print(f'Used memory is {count_mem}')

# переменных 6 штук, памяти требуется меньше (308)
# python 3.7.2 32-bit