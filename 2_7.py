# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел 
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input("Enter a natural number, please: "))

i = 0
summ = 0

while i < n:
    i = i + 1
    summ = summ + i

print(f"The calculated value of the sum is {summ}")
summFormula = int(n * (n + 1) / 2)
print(f"The calculated value (Formula) of the sum is {summFormula}")

if summ == summFormula:
    print("Formula is correct!")
else:
    print("Formula is incorrect!")