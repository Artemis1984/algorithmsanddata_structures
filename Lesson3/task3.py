# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random
rand_list = [random.randint(0, 100) for i in range(10)]
print(rand_list)
min_num = 100
max_num = 0

for number in rand_list:
    if number < min_num:
        min_num = number
    elif number > max_num:
        max_num = number

rand_list[rand_list.index(min_num)], rand_list[rand_list.index(max_num)] = max_num, min_num
print(rand_list)

