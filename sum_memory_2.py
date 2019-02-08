# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# (в рамках первых трех уроков)

import sys


def sum_memory(objects):
    sum_mem = 0
    for item in objects:
        if item.startswith('__'):
            # убираем "магию"
            continue
        elif hasattr(objects[item], '__call__'):
            # убираем функции
            continue
        elif hasattr(objects[item], '__loader__'):
            # убираем модули
            continue
        else:
            if hasattr(objects[item], '__iter__'):
                if hasattr(objects[item], 'items'):
                    for key, value in objects[items]:
                        #self._add(key)
                        #self._add(value)
                        sum_mem += sys.getsizeof(key)
                        sum_mem += sys.getsizeof(value)
                elif not isinstance(objects[item], str):
                    for value in objects[item]:
                        sum_mem += sys.getsizeof(value)
            sum_mem += sys.getsizeof(objects[item])
            print(f'переменная {item} класса {type(objects[item])} хранит {objects[item]} '
                  f'и занимает {sys.getsizeof(objects[item])} байт')

    return sum_mem

