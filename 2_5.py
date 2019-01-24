# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 
# 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.


print("ASCII character table 32 through 127 inclusive")

i = 32
j = 0
string = ""

while i <= 127:
    
    string = string + str(i) + " " + str(chr(i)) + "    "
    i = i + 1
    j = j + 1
    if ((j % 10) == 0) or (i == 128):
        print(string)
        string = ""
    