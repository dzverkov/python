# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках.

import random


def get_median(ar, k):

    if len(ar) == 1:
        return ar[0]

    pivot = random.choice(ar)

    small_arr = []
    medium_arr = []
    large_arr = []

    for item in ar:
        if item < pivot:
            small_arr.append(item)
        elif item == pivot:
            medium_arr.append(item)
        elif item > pivot:
            large_arr.append(item)

    if k < len(small_arr):
        return get_median(small_arr, k)
    elif k < len(small_arr) + len(medium_arr):
        return medium_arr[0]
    else:
        return get_median(large_arr, k - len(small_arr) - len(medium_arr))


M = 10
MIN_LIMIT = 0
MAX_LIMIT = 100

array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(2*M+1)]
print(array)
# print(sorted(array))
m = get_median(array, len(array) // 2)
print(m)
