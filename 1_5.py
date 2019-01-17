print("Write two letters")
a = str(input('Write first letter: '))
b = str(input('Write second letter: '))


import random
x = ord(a)
y = ord(b)
print('Number of first letter is ' + str(x))
print('Number of second letter is ' + str(y))

z = abs(x-y) - 1

if z < 0:
	z = 0
    
print('Number of second letters between is ' + str(z))
