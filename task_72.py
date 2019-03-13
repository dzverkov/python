# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
# случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def sort_merge(ar):
    if len(ar) > 1:
        mid = len(ar)//2
        left = ar[:mid]
        right = ar[mid:]

        sort_merge(left)
        sort_merge(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                ar[k] = left[i]
                i = i + 1
            else:
                ar[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            ar[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            ar[k] = right[j]
            j = j + 1
            k = k + 1


SIZE = 10
MIN_LIMIT = 0
MAX_LIMIT = 50
array = [random.uniform(MIN_LIMIT, MAX_LIMIT - 1e-10) for _ in range(SIZE)]

print(array)
sort_merge(array)
print(array)
