# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках практического задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# Определить, какое число в массиве встречается чаще всего.
# Числа целые положительные, начиная с нуля (MIN_LIMIT = 0, MAX_LIMIT >= 0)

import random
import collections
import cProfile

def create_array(size, max_num_value):
    min_limit = 0
    max_limit = max_num_value
    array = [random.randint(min_limit, max_limit) for _ in range(size)]
    # print(array)
    return array


# Для подсчёта частоты вхождения используется словарь
def find_freq_num_1(ar):

    num_dict = dict()

    for item in ar:
        if item in num_dict.keys():
            num_dict[item] += 1
        else:
            num_dict[item] = 1

    m_val = 0
    m_num = 0

    for num, value in num_dict.items():
        if m_val <= value:
            m_val = value
            m_num = num

    # print(num_dict)
    print(f"Чаще всего встречается число: {m_num}")


# Для подсчёта частоты вхождения используется словарь с использованием collections.defaultdict
def find_freq_num_2(ar):

    num_dict = collections.defaultdict(int)

    for item in ar:
        num_dict[item] += 1

    m_val = 0
    m_num = 0

    for num, value in num_dict.items():
        if m_val <= value:
            m_val = value
            m_num = num

    # print(num_dict)
    print(f"Чаще всего встречается число: {m_num}")


# Для подсчёта частоты вхождения используется массив с размерностью max_num_value
def find_freq_num_3(ar, max_num_value):

    freq_ar = [0] * (max_num_value + 1)

    for item in ar:
        freq_ar[item] += 1

    m_val = 0
    m_num = 0

    for i in range(len(freq_ar)):
        if m_val <= freq_ar[i]:
            m_val = freq_ar[i]
            m_num = i
    # print(freq_ar)
    print(f"Чаще всего встречается число: {m_num}")


# Для подсчёта частоты вхождения используется модуль collections
def find_freq_num_4(ar):
    num_dict = collections.Counter(ar)
    print(f"Чаще всего встречается число: {num_dict.most_common(1)[0][0]}")


def start_all(size, max_num_value):

    ar = create_array(size, max_num_value)

    find_freq_num_1(ar)
    find_freq_num_2(ar)
    find_freq_num_3(ar, max_num_value)
    find_freq_num_4(ar)


def start_n(func_num, size, max_num_value):

    ar = create_array(size, max_num_value)

    if func_num == 1:
        find_freq_num_1(ar)
    elif func_num == 2:
        find_freq_num_2(ar)
    elif func_num == 3:
        find_freq_num_3(ar, max_num_value)
    elif func_num == 4:
        find_freq_num_4(ar)


# cProfile.run("start_all(10000000,10000)")

# cProfile tests
#################################################################################
# test 1
# cProfile.run("start_all(10000,100)")
#         1    0.000    0.000    0.214    0.214 task-41.py:19(create_array)
#         1    0.021    0.021    0.029    0.029 task-41.py:28(find_freq_num_1)
#         1    0.012    0.012    0.012    0.012 task-41.py:51(find_freq_num_2)
#         1    0.008    0.008    0.008    0.008 task-41.py:71(find_freq_num_3)
#         1    0.000    0.000    0.005    0.005 task-41.py:90(find_freq_num_4)
#         1    0.000    0.000    0.269    0.269 task-41.py:96(start_all)

# test 2
# cProfile.run("start_all(10000000,100)")
#         1    0.000    0.000  141.956  141.956 task-41.py:19(create_array)
#         1   16.057   16.057   19.485   19.485 task-41.py:28(find_freq_num_1)
#         1    6.046    6.046    6.046    6.046 task-41.py:51(find_freq_num_2)
#         1    5.019    5.019    5.019    5.019 task-41.py:71(find_freq_num_3)
#         1    0.000    0.000    3.536    3.536 task-41.py:90(find_freq_num_4)
#         1    0.000    0.000  176.042  176.042 task-41.py:96(start_all)

# test 3
# cProfile.run("start_all(10000000,10000)")
#         1    0.000    0.000  134.743  134.743 task-41.py:19(create_array)
#         1   18.541   18.541   21.685   21.685 task-41.py:28(find_freq_num_1)
#         1    8.445    8.445    8.445    8.445 task-41.py:51(find_freq_num_2)
#         1    4.920    4.920    4.920    4.920 task-41.py:71(find_freq_num_3)
#         1    0.000    0.000    5.821    5.821 task-41.py:90(find_freq_num_4)
#         1    0.005    0.005  175.618  175.618 task-41.py:95(start_all)
#################################################################################

# timeit
#################################################################################
# Test find_freq_num_1
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(1, 1000, 10)"
# 100 loops, best of 5: 12.2 msec per loop
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(1, 10000, 1000)"
# 100 loops, best of 5: 109 msec per loop

# Test find_freq_num_2
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(2, 1000, 10)"
# 100 loops, best of 5: 12.3 msec per loop
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(2, 10000, 1000)"
# 100 loops, best of 5: 104 msec per loop

# Test find_freq_num_3
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(3, 1000, 10)"
# 100 loops, best of 5: 14.5 msec per loop
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(3, 10000, 1000)"
# 100 loops, best of 5: 95 msec per loop

# Test find_freq_num_4
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(4, 1000, 10)"
# 100 loops, best of 5: 16.2 msec per loop
# python.exe -m timeit -n 100 -s "import task_41" "task_41.start_n(4, 10000, 1000)"
# 100 loops, best of 5: 101 msec per loop

# Вывод
#################################################################################
# Вариант 1 самый медленный, за счет постояннонго поиска элементов в словаре.
# В варианте 2 был устранён недостаток варианта 2, что привело к резкому росту производительности.
# В варианте 3 использование массива позволило избавиться от операций поиска элементов, что еще увеличило скорость,
# но за счет увеличения потребления памяти (большая часть которой может и не использоваться при большом max_num_value).
# Вариант 3 в одном из тестов даже обогнал реализацию на функциях стандартной библиотеки (Вариант 4).
# Вариант 4 почти всегда выигрывает по производительности, за счет того, что библиотеки написаны на С
