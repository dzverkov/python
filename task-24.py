
n = int(input("Введите количество елементов:"))

if n <= 0:
    print("Число должно быть целым положительным.")
    quit()

first_elem = 1
num = first_elem
sum = 0
s = ""

while True:
    sum += num
    s = s + str(num) + " "
    n -=1
    num = -num/2

    if n == 0:
        print(f"Последовательность:{s}")
        print(f"Сумма чисел последовательности:{sum}")
        break
