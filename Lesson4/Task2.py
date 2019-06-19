# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность алгоритмов.

import timeit
import cProfile


sim1 = """
n = 100
simple_list = []
for i in range(2, n * n):
    if len(simple_list) == n:
        break
    for j in range(2, i + 1):
        if i % j == 0 and i != j:
            break
        elif i % j == 0 and i == j:
            simple_list.append(i)


"""

print("обычная программа", timeit.timeit(sim1, number=100))

eratos = """
n = 100
a = [i for i in range(n * n)]
a[1] = 0

for m in range(2, len(a)):
    if a[m] != 0:
        for s in range(m * 2, len(a), m):
            a[s] = 0

b = []
for i in range(0, len(a), ):
    if a[i] != 0:
        b.append(a[i])



"""
print("метод Ератосфена", timeit.timeit(eratos, number=100))


# обычная программа 0.28099336399999997
# метод Ератосфена 0.32427037700000005


def simple_number1(n):
    simple_list = []
    for i in range(2, n * n):
        if len(simple_list) == n:
            break
        for j in range(2, i + 1):
            if i % j == 0 and i != j:
                break
            elif i % j == 0 and i == j:
                simple_list.append(i)

    return simple_list[n - 1]


cProfile.run("simple_number1(100)")


def simple_eratosfen(n):
    a = [i for i in range(n * n)]
    a[1] = 0

    for m in range(2, len(a)):
        if a[m] != 0:
            for s in range(m * 2, len(a), m):
                a[s] = 0

    b = []
    for i in range(0, len(a), ):
        if a[i] != 0:
            b.append(a[i])

    return b[n - 1]


cProfile.run("simple_eratosfen(100)")


#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#        1    0.003    0.003    0.003    0.003 Task2.py:52(simple_number1)
#        1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#      541    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.003    0.003    0.004    0.004 Task2.py:69(simple_eratosfen)
#         1    0.000    0.000    0.000    0.000 Task2.py:70(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#      1231    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Мне кажется, что у меня хуже всего организовано заполнение массива в начале,
# так как я не знаю сколько элементов нужно, чтобы добратся до необходимого простого числа
# Я ожидал, что Эратосфен будет работать быстрее, но у меня оказалось иначе.
