# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
# отсортированный массивы.


import random
import cProfile

size = int(input("Введите размер массива:"))

array = [float("%.1f" % random.uniform(0, 49)) for i in range(size)]


print(array)


def merger(array):

    sorted_list = []
    for i in range(1, len(array), 2):

        sorted_list.append([array[i-1], array[i]])

    if len(array) % 2 != 0:
        sorted_list.append([array[len(array)-1]])

    for i in range(len(sorted_list)):
        if len(sorted_list[i]) == 1:
            continue
        if len(sorted_list) % 2 != 0:
            if i == len(sorted_list) - 1:
                break
        for j in range(1):
            if sorted_list[i][j] > sorted_list[i][j+1]:
                sorted_list[i][j], sorted_list[i][j+1] = sorted_list[i][j+1], sorted_list[i][j]

    temp_list = []
    i = 0
    flag = False
    while True:

        if sorted_list[i][i] <= sorted_list[i + 1][i]:

            temp_list.append(sorted_list[i][i])

            del sorted_list[i][i]

        else:
            temp_list.append(sorted_list[i + 1][i])
            del sorted_list[i + 1][i]

        if len(sorted_list[i]) == 0:
            temp_list.extend(sorted_list[i+1])
            del sorted_list[i+1], sorted_list[i]
            flag = True

        elif len(sorted_list[i+1]) == 0:
            temp_list.extend(sorted_list[i])
            del sorted_list[i+1], sorted_list[i]
            flag = True

        if flag:
            sorted_list.append(temp_list[:])
            temp_list.clear()
            flag = False

        if len(sorted_list) == 1:
            break

    print(*sorted_list)


merger(array)
print(cProfile.run("merger(array)"))

# Возможно немного хардкожено, но алгоритм написал сам, без какой либо помощи)

# Замер на 10000 элементов

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.177    0.177 <string>:1(<module>)
#         1    0.141    0.141    0.176    0.176 Task_2.py:17(merger)
#         1    0.000    0.000    0.177    0.177 {built-in method builtins.exec}
#    355041    0.023    0.000    0.023    0.000 {built-in method builtins.len}
#         1    0.003    0.003    0.003    0.003 {built-in method builtins.print}
#    125856    0.009    0.000    0.009    0.000 {method 'append' of 'list' objects}
#      4999    0.001    0.000    0.001    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      4999    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

# Замер на 100000

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.115    4.115 <string>:1(<module>)
#         1    3.663    3.663    4.114    4.114 Task_2.py:17(merger)
#         1    0.000    0.000    4.115    4.115 {built-in method builtins.exec}
#   4550540    0.296    0.000    0.296    0.000 {built-in method builtins.len}
#         1    0.036    0.036    0.036    0.036 {built-in method builtins.print}
#   1591946    0.107    0.000    0.107    0.000 {method 'append' of 'list' objects}
#     49999    0.007    0.000    0.007    0.000 {method 'clear' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     49999    0.005    0.000    0.005    0.000 {method 'extend' of 'list' objects}


# Этот вариант гораздо быстрее других, я даже не ожидал такого результата)
