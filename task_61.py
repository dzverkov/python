# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Задача 3.8
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# Примечание: Для удобства немного изменил условия. Матрица генерится, а не вводится вручную и сразу сохраняется в
# ту или иную структуру данных. Размер матрицы произвольный.
# При подсчёте занимаемой памяти производится проверка на уже используемый объект.
# Локальные переменные считаются один раз (можно считать при каждом новом присвоении), здесь не стал усложнять

import sys
import random
from collections import namedtuple, deque


def get_mem_size(x, ids):

    if id(x) in ids:
        return 0

    res = sys.getsizeof(x)
    ids.add(id(x))

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                res += get_mem_size(key, ids)
                res += get_mem_size(value, ids)
        elif not isinstance(x, str):
            for item in x:
                res += get_mem_size(item, ids)
    return res


# Матрица хранится в списках
def matrix_sum_array(mp, fl_print_res=True, ids=set()):
    mem_used = 0
    m = [[random.randint(mp.min_limit, mp.max_limit) for _ in range(mp.n)] for _ in range(mp.m)]

    sum_row = 0
    for item in m:
        sum_row = sum(item)
        # Добавим сумму в конец строки
        item.append(sum_row)

    # Распечатаем результат
    i = 0  # обьявление для подсчёта занимаемой памяти
    if fl_print_res:
        for i in range(len(m)):
            for item in m[i]:
                print("{:4d}".format(item), end='\t')
            print()

    mem_used += get_mem_size(m, ids)
    mem_used += get_mem_size(sum_row, ids)
    mem_used += get_mem_size(i, ids)
    return mem_used


# Матрица хранится в очередях
def matrix_sum_deque(mp, fl_print_res=True, ids=set()):
    mem_used = 0
    m = deque()

    for _ in range(mp.m):
        m.append(deque([random.randint(mp.min_limit, mp.max_limit) for _ in range(mp.n)]))

    sum_row = 0
    for item in m:
        sum_row = sum(item)
        # Добавим сумму в конец строки
        item.append(sum_row)

    # Распечатаем результат
    i = 0  # обьявление для подсчёта занимаемой памяти
    if fl_print_res:
        for i in range(len(m)):
            for item in m[i]:
                print("{:4d}".format(item), end='\t')
            print()

    mem_used += get_mem_size(m, ids)
    mem_used += get_mem_size(sum_row, ids)
    mem_used += get_mem_size(i, ids)
    return mem_used


# Матрица хранится в словарях
def matrix_sum_dict(mp, fl_print_res=True, ids=set()):
    mem_used = 0
    m = {i: {j: random.randint(mp.min_limit, mp.max_limit) for j in range(mp.n)} for i in range(mp.m)}

    sum_row = 0
    for item in m.values():
        sum_row = sum(item.values())
        # Добавим сумму в конец строки
        item["row_sum"] = sum_row

    # Распечатаем результат
    i = 0  # обьявление для подсчёта занимаемой памяти
    if fl_print_res:
        for i in range(len(m)):
            for item in m[i].values():
                print("{:4d}".format(item), end='\t')
            print()

    mem_used += get_mem_size(m, ids)
    mem_used += get_mem_size(sum_row, ids)
    mem_used += get_mem_size(i, ids)
    return mem_used


def main():
    MatrixParam = namedtuple('MatrixParam', ['n', 'm', 'min_limit', 'max_limit'])
    mp = MatrixParam(n=100, m=100, min_limit=300, max_limit=400)

    mx_par_mem_used = get_mem_size(mp, set())

    print(f"Версия Python: {sys.version}")
    print(f"Параметры матрицы: {mp}")
    # Для хранения адресов объектов
    print("Матрица хранится в списках")
    mem_used = matrix_sum_array(mp, False)
    print(f"Занимаемая память: {mem_used + mx_par_mem_used} байт.")
    print("Матрица хранится в очередях")
    mem_used = matrix_sum_deque(mp, False)
    print(f"Занимаемая память: {mem_used + mx_par_mem_used} байт.")
    print("Матрица хранится в словарях")
    mem_used = matrix_sum_dict(mp, False)
    print(f"Занимаемая память: {mem_used + mx_par_mem_used} байт.")


if __name__ == "__main__":
    main()


# Результаты тестирования
############################################################
# Версия Python: 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Параметры матрицы: MatrixParam(n=100, m=100, min_limit=0, max_limit=100)
# Матрица хранится в списках
# Занимаемая память: 97868 байт.
# Матрица хранится в очередях
# Занимаемая память: 123444 байт.
# Матрица хранится в словарях
# Занимаемая память: 480916 байт.
############################################################
# Версия Python: 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Параметры матрицы: MatrixParam(n=100, m=100, min_limit=300, max_limit=400)
# Матрица хранится в списках
# Занимаемая память: 375100 байт.
# Матрица хранится в очередях
# Занимаемая память: 400676 байт.
# Матрица хранится в словарях
# Занимаемая память: 760920 байт.
############################################################
