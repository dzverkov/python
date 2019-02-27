# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 100
MIN_LIMIT = -100
MAX_LIMIT = 100
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

max_negative_num = 0
max_negative_num_idx = 0

for i in range(len(array)):
    if array[i] < 0:
        if max_negative_num == 0:
            max_negative_num = array[i]
        elif max_negative_num < array[i]:
            max_negative_num = array[i]
            max_negative_num_idx = i

print(f"Максимальный отрицательный элемент: {max_negative_num}")
print(f"Позиция максимального отрицательного элемента: {max_negative_num_idx}")
