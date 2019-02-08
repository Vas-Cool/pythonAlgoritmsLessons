# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.



import random
from sum_memory_2 import sum_memory



"""
Функция quick_sort находит к-ю статистику в массиве
Основана на функции быстрой сортировки
делим массив случайным образом, далее перекидываем элементы, которые меньше случайно выбранного элемента в массиы small
массив medium содержит элементы, равные случайно выбранному, lsrge - элементы больше выбранного.
Далее либо м нашли к-ю статистику, либо запускаем рекурсию.
"""
def quick_sort(array, k):
    # print(k)
    if len(array) == 1:
        return array[0]
    pivot = random.choice(array)
    small = []
    medium = []
    large = []

    for item in array:
        if item < pivot:
            small.append(item)
        elif item == pivot:
            medium.append(item)
        elif item > pivot:
            large.append(item)


    if len(small) > k:
        return quick_sort(small, k)
    elif len(small) + len(medium) > k:
        return pivot
    else:
        return quick_sort(large, k - len(small) - len(medium))


def find_median(array_):

    if len(array_) % 2 == 0:
        return None
    k = (len(array_) + 1) / 2

    return quick_sort(array_, k - 1)



SIZE = 11
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

array = [3, 8, 8, 6, 6, 4, 10, 1, 9, 6, 10]
# array = [1,2,3,4,5,6,7,8,9]
print(array)
print(find_median(array))

print(sum_memory(locals()))