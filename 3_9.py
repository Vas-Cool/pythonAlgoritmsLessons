#Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE_X = 5
SIZE_Y = 3
MIN_ITEM = 1
MAX_ITEM = 10

matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_X)] for _ in range(SIZE_Y)]
for line in matrix:
    print(line)

min_column = [MAX_ITEM] * len(matrix[0])
print(min_column)
print('*' * SIZE_X * 2)

for line in matrix:
    sum_line = 0

    for i, item in enumerate(line):
        #sum_line += item
        if min_column[i] > item:
        	min_column[i] = item
        print(f'{item:^5}', end='')

    print(f' | {sum_line}')

max_min = MIN_ITEM
for item in min_column:
    print(f'{item:^5}', end='')
    if item > max_min:
    	max_min = item
print('\n', max_min)
