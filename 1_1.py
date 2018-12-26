print("Write three-digit number")
a = int(input('Write three-digit number: '))


x = (a - (a % 100))/100
y = (a % 100 - a % 10)/10
z = (a % 10)

print("Sum of digits is")
print(x + y + z)

print("Multiple of digits is")
print(x * y * z)