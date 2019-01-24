from collections import defaultdict
from collections import deque

# создание справочника шестнадцетиричных цифр
digits = '0123456789abcdef'
dict_of_digits = defaultdict(str)
i = 0
for char in digits:
    dict_of_digits[char] = i
    i = i + 1
print(dict_of_digits) #проверка корректности справочника 16-х цифр

a_10 = int(input('Введите первое слагаемое в 10-й системе: '))
b_10 = int(input('Введите первое слагаемое в 10-й системе: '))
if a_10 < b_10:
    x = b_10
    b_10 = a_10
    a_10 = x

a_16_str = str(hex(a_10))
b_16_str = str(hex(b_10))

a_16 = deque()
b_16 = deque()

i = 1
for char in a_16_str:
    a_16.appendleft(char)
    if i <= len(b_16_str):
        b_16.appendleft(b_16_str[i-1])
    i = i + 1
a_16.pop()
a_16.pop()
b_16.pop()
b_16.pop()

print(a_16_str, b_16_str, sep='\n')

temp = 0
result_16=deque()

i = 1
x = 0
y = 0
z = 0
for char in a_16:
    x = int(dict_of_digits[char])
    if i <= len(b_16):
        y = int(dict_of_digits[b_16[i-1]])
    if (x + y + temp) < 16:
        z = (x + y + temp)
        temp = 0
    else:
        z = (x + y + temp) % 16
        temp = 1
    result_16.appendleft(digits[z])
    y = 0
    i = i + 1

if temp == 1:
    result_16.appendleft('1')
result_16.appendleft(str('x'))
result_16.appendleft('0')

print(''.join(result_16))


