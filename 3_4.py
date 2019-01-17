#Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_index = 0
max_count = 1

for i in range(SIZE):
	count_i = 0
	for j in range(SIZE):
		if array[j] == array[i]:
			count_i += 1
	if count_i > max_count:
		max_count = count_i
		max_index = i

print(array[max_index], max_index, max_count)