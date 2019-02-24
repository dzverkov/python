
while True:
    n1=int(input("Введите первое число:"))
    n2=int(input("Введите второе число:"))

    while True:
        op=input("Введите операцию ('0', '+', '-', '*', '/'):")

        if op not in "0+-*/":
            print("Операция неизвестна, повторите ввод операции.")
        else:
            break

    if op == '0':
        break

    if op == '/' and n2 == 0:
        print("Деление на ноль! Повторите ввод.")
        continue

    if op == '+':
        res = n1 + n2
    elif op == '-':
        res = n1 - n2
    elif op == '*':
        res = n1 * n2
    else:
        res = n1 / n2

    print(f"{n1} {op} {n2} = {res}")