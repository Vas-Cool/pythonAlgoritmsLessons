# ����� ����� n ��������� ���������� ���� �����: 1 -0.5 0.25 -0.125 ...
# ���������� ��������� (n) �������� � ����������.

n = int(input('Enter the number of series elements, please: '))
b = 1
i = 1
c = b

while i < n:
    b = b * -0.5
    i = i + 1
    c = c + b
    
print("The summ is",c)
