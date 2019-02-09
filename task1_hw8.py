import hashlib

"""
Функция subs_count считает кольчество уникальных срок в подсроке
param s - срока, в которой нужно найти подстроки
return - количество найденных уникальных подстрок в строке s
"""
def subs_count(string):
    len_string = len(string)
    if len_string == 1:
        return 0
    string = string.encode('utf-8')
    subs = []
    # размер подстроки от 1 до длины строки минус 1
    for i in range(1, len_string):
        # подстрока начинается с различных мест в подстроке: от 1 до длина строки минус длина подстроки
        for j in range(len_string - i + 1):
            hash_sub = hash(string[j:j + i])
            print(string[j:j + i], hash_sub)
            if hash_sub not in subs:
                subs.append(hash_sub)
    print(subs)
    return len(subs)


string = input('Введите строку: ')
print(f'Количество уникальных подстрок {subs_count(string)}')