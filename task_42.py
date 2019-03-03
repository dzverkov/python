# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования Решета Эратосфена;
# Использовать алгоритм решето Эратосфена


def get_prime_eratosthenes(n, max_num=10000):

    cnt = 0

    a = [i for i in range(max_num)]
    a[1] = 0

    m = 2
    while m < max_num:  # перебор всех элементов
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            cnt += 1
            if cnt == n:
                return a[m]

            while j < max_num:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    print("Число не найдено, необходимо увеличить параметр max_num")


def get_prime_simple(n):
    num = 0
    cnt = 0

    while True:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                cnt += 1
                if cnt == n:
                    return num
        num += 1


# print(get_prime_simple(3))
# print(get_prime_eratosthenes(3))

# Test results
# get_prime_simple(10)
# 10 loops, best of 5: 115 usec per loop
# get_prime_simple(100)
# 10 loops, best of 5: 10.3 msec per loop
# get_prime_simple(1000)
# 10 loops, best of 5: 1.83 sec per loop

# get_prime_eratosthenes(10)
# 10 loops, best of 5: 13.1 msec per loop
# get_prime_eratosthenes(100)
# 10 loops, best of 5: 22.6 msec per loop
# get_prime_eratosthenes(1000)
# 10 loops, best of 5: 16.2 msec per loop

# Применение алгоритма решета Эратосфена существенно быстрее простого алгоритма, но требует предварительного
# выделения памяти.

