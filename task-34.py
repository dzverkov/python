# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 100
MIN_LIMIT = 0
MAX_LIMIT = 10
array = [random.randint(MIN_LIMIT, MAX_LIMIT) for _ in range(SIZE)]
print(array)

num_dict = dict()

for i in range(len(array)):
    if array[i] in num_dict.keys():
        num_dict[array[i]] += 1
    else:
        num_dict[array[i]] = 1

m_val = 0
m_num = 0

for num, value in num_dict.items():
    if m_val < value:
        m_val = value
        m_num = num

# print(num_dict)
print(f"Чаще всего встречается число: {m_num}")
