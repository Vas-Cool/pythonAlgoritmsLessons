# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не 
# должна завершаться, а должна запрашивать новые данные для вычислений. Завершение 
# программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об 
# ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности 
# деления на ноль, если он ввел 0 в качестве делителя.

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