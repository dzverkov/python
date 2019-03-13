# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

def sort_buble(ar):
    last_swap_pos = len(ar) - 1
    fl_swap = True
    while fl_swap:
        fl_swap = False
        for i in range(last_swap_pos):
            if ar[i] < ar[i + 1]:
                ar[i], ar[i + 1] = ar[i + 1], ar[i]
                last_swap_pos = i + 1
                fl_swap = True


SIZE = 100
MIN_LIMIT = -100
MAX_LIMIT = 100
array = [random.randint(MIN_LIMIT, MAX_LIMIT-1) for _ in range(SIZE)]

# =============================================================================================
# Для тестов
# Полностью отсортированный массив, должен быть один проход массива
# array = sorted([random.randint(MIN_LIMIT, MAX_LIMIT-1) for _ in range(SIZE)], reverse=True)
# Частично отсортированный массив, тестирование запоминания последней позиции перестановки
# array = [random.randint(MAX_LIMIT//2, MAX_LIMIT-1) for _ in range(SIZE//2)] \
#        + sorted([random.randint(MIN_LIMIT, MAX_LIMIT//2) for _ in range(SIZE//2)], reverse=True)
# =============================================================================================
print(array)
sort_buble(array)
print(array)
