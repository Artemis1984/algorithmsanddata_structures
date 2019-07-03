# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и
# отсортированный массивы.

import random
import cProfile


array = [random.randint(-100, 99) for i in range(100000)]


def bubble_sort_1(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]


def bubble_sort_2(array):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] <= array[j]:
                array.insert(i, array.pop(j))


def bubble_sort_original(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1


print("Исходный массив:", array)

# bubble_sort_original(array)
bubble_sort_1(array)
# bubble_sort_2(array)

print("Отсортированный:", array)

# print(cProfile.run('bubble_sort_original(array)'))
print(cProfile.run('bubble_sort_1(array)'))
# print(cProfile.run('bubble_sort_2(array)'))


# Замеры на 10000 элементов

# Вариант из методички

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.274    5.274 <string>:1(<module>)
#         1    5.272    5.272    5.274    5.274 Task_1.py:26(bubble_sort_original)
#         1    0.000    0.000    5.275    5.275 {built-in method builtins.exec}
#     19999    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# вариант 1

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    4.729    4.729 <string>:1(<module>)
#         1    4.728    4.728    4.729    4.729 Task_1.py:12(bubble_sort_1)
#         1    0.000    0.000    4.729    4.729 {built-in method builtins.exec}
#     10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# вариант 2

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    5.746    5.746 <string>:1(<module>)
#         1    4.779    4.779    5.746    5.746 Task_1.py:19(bubble_sort_2)
#         1    0.000    0.000    5.746    5.746 {built-in method builtins.exec}
#     10001    0.001    0.000    0.001    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#    249120    0.692    0.000    0.692    0.000 {method 'insert' of 'list' objects}
#    249120    0.274    0.000    0.274    0.000 {method 'pop' of 'list' objects}

# Замеры на 100000 элементов

# Вариант из методички

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000  524.924  524.924 <string>:1(<module>)
#         1  524.883  524.883  524.924  524.924 Task_1.py:26(bubble_sort_original)
#         1    0.000    0.000  524.924  524.924 {built-in method builtins.exec}
#    199999    0.040    0.000    0.040    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вариант 1

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000  480.099  480.099 <string>:1(<module>)
#         1  480.059  480.059  480.099  480.099 Task_1.py:12(bubble_sort_1)
#         1    0.000    0.000  480.099  480.099 {built-in method builtins.exec}
#    100001    0.039    0.000    0.039    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Не ну здесь наверное random.shuffle() быстрее сработает:)
