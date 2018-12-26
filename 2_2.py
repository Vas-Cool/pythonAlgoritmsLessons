# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 
# 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input('Write a number, please: '))
i = 0
j = 0

for dig in str(a):
    if ((int(dig) + 0) % 2) > 0:
        i = i + 1
    else:
        j = j + 1
        
print("Number of odd digits is",i)
print("Number of even digits is",j)