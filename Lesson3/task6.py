# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

rand_list = [random.randint(0, 100) for i in range(25)]
print(rand_list)

min_num = 100
min_num_index = None
max_num = -1
max_num_index = None
sum_ = 0

for item in rand_list:
    if item < min_num:
        min_num = item
        min_num_index = rand_list.index(min_num)
    elif item > max_num:
        max_num = item
        max_num_index = rand_list.index(max_num)

print(f"Минимальный элемент: {min_num}, под индексом: {min_num_index}, "
      f"максимальный элемент {max_num}, под индексом: {max_num_index}")


if max_num_index - min_num_index < 0:
    for i in range(max_num_index + 1, min_num_index):
        sum_ += rand_list[i]
else:
    for i in range(min_num_index + 1, max_num_index):
        sum_ += rand_list[i]

print(f"Сумма элементов между минимальным и максимальным элементами: {sum_}")
