# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random
import cProfile


def shell_sort(array):
    def new_increment(a):
        i = int(len(a) / 2)
        yield i
        while i != 1:
            if i == 2:
                i = 1
            else:
                i = int(i / 2.2)
            yield i

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] < array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
    return array


m = int(input("Введите натуральное число:"))
array = [random.randint(0, 100) for i in range(m)]


print("Исходный массив:", array)

array = shell_sort(array)
print("Отсортированный:", array)

if len(array) % 2 != 0:
    print("Медианой массива является число: ", array[len(array) - len(array) // 2 - 1])

else:
    print("Медианой массива является число:", (array[(len(array) - len(array) // 2 - 1)] +
          array[(len(array) - len(array) // 2)]) / 2)


print(cProfile.run("shell_sort(array)"))

# Если честно я сортировку Шелла взял из методички))
# Но жуком прошелся многое стало понятно. Думаю секрет в этих формулах:
# i = int(len(a) / 2)
# i = int(i / 2.2)
# А медиана выводится и при четном размере массива

# Замер на 10000 элементов

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.278    0.278 <string>:1(<module>)
#         1    0.278    0.278    0.278    0.278 Task_3.py:8(shell_sort)
#        12    0.000    0.000    0.000    0.000 Task_3.py:9(new_increment)
#         1    0.000    0.000    0.278    0.278 {built-in method builtins.exec}
#        12    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Замер на 100000 элементов

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   24.008   24.008 <string>:1(<module>)
#         1   24.008   24.008   24.008   24.008 Task_3.py:8(shell_sort)
#        15    0.000    0.000    0.000    0.000 Task_3.py:9(new_increment)
#         1    0.000    0.000   24.008   24.008 {built-in method builtins.exec}
#        15    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
