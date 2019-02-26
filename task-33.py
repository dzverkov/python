# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_LIMIT = 0
MAX_LIMIT = 1000
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

min_num_index = 0
max_num_index = 0

for i in range(len(array)):
    if array[i] < array[min_num_index]:
        min_num_index = i
    if array[i] > array[max_num_index]:
        max_num_index = i

if min_num_index != max_num_index:
    array[min_num_index], array[max_num_index] = array[max_num_index], array[min_num_index]

print(array)
