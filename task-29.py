def calc_sum(n):
    d = 10

    if n == 0:
        return 0
    else:
        num = n % d
        return num + calc_sum(n // d)


max_num = 0
max_sum = 0

while True:
    nr = int(input("Введите число:"))

    if nr == 0:
        print(f"Число {max_num} -> {max_sum}")
        quit()

    num_sum = calc_sum(nr)

    if num_sum >= max_sum:
        max_num = nr
        max_sum = num_sum
