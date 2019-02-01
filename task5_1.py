from collections import deque
from collections import namedtuple

n = int(input('Введите количество компаний: '))
a = deque()
average_year_income = 0
Company = namedtuple('Company', 'name, year_income')

for i in range(n):
    print(i)
    name = str(input('Введите название Предприятия: '))
    q1 = float(input('Введите значение прибыли за первый квартал: '))
    q2 = float(input('Введите значение прибыли за второй квартал: '))
    q3 = float(input('Введите значение прибыли за третий квартал: '))
    q4 = float(input('Введите значение прибыли за четвертый квартал: '))
    year_income = q1 + q2 + q3 + q4
    cur_company = Company(name, year_income)
    a.append(cur_company)
    average_year_income = average_year_income + year_income

average_year_income = average_year_income / n

print('Предприятия с прибылью выше среднего:')
for elem in a:
    if elem.year_income > average_year_income:
        print(elem.name)
        
print('Предприятия с прибылью ниже среднего:')
for elem in a:
    if elem.year_income < average_year_income:
        print(elem.name)
