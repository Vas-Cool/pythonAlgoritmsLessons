# �������� ���������, ������� ����� ����������, ��������, �������� ��� ������ ��� �����. 
# ����� � ���� �������� �������� �������������. ����� ���������� ���������� ��������� �� 
# ������ �����������, � ������ ����������� ����� ������ ��� ����������. ���������� 
# ��������� ������ ����������� ��� ����� ������� '0' � �������� ����� ��������. 
# ���� ������������ ������ �������� ���� (�� '0', '+', '-', '*', '/'), �� ��������� ������ �������� ��� �� 
# ������ � ����� ����������� ���� ��������. ����� �������� ������������ � ������������� 
# ������� �� ����, ���� �� ���� 0 � �������� ��������.

while True:
    operator = str(input('Write an operator (+ - * /), please 0 - Exit: '))
    if operator == "0":
        break
    elif (operator == "+") or (operator == "-") or (operator == "*") or (operator == "/"):
        a = int(input('Write a first number, please: '))
        while True:
            b = int(input('Write a second number, please: '))
            if (operator == "/") and (b == 0):
                print('Division on zero is not possible.')
            else:
                break
        if operator == "+":
            print("The resut is: ", a + b)
        elif operator == "-":
            print("The resut is: ", a - b)
        elif operator == "*":
            print("The resut is: ", a * b)

        elif operator == "/":
                print("The resut is: ", a / b)
    else:
        print("The operator is wrong")
print("Goodbye")