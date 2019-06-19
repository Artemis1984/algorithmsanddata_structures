# Посчитать четные и нечетные цифры введенного натурального числа. Например,
# если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

# Задание модифицировал для более наглядного отображения результатов работы программ

import timeit
import cProfile

program1 = """


number = [str(i) for i in range(10000)]
first_list = []
second_list = []

for num in number:
    if int(num) % 2 == 0:
        first_list.append(num)

for num in number:
    if int(num) % 2 != 0:
        second_list.append(num)

"""

print("программа 1", timeit.timeit(program1, number=100))


program2 = """

number = [i for i in range(10000)]
first_list = []
second_list = []

for num in number:
    if num % 2 == 0:
        first_list.append(num)

for num in number:
    if num % 2 != 0:
        second_list.append(num)

"""
print("программа 2", timeit.timeit(program2, number=100))


program3 = """

number = [i for i in range(10000)]
first_list = []
second_list = []
for num in number:
    if num % 2 == 0:
        first_list.append(num)
    else:
        second_list.append(num)

"""
print("программа 3", timeit.timeit(program3, number=100))

# программа 1 - 0.862798577
# программа 2 - 0.21250937000000014
# программа 3 - 0.14331741899999995

# первый вариант умышленно усложнил перобразованиями элементов в str и обратно в int
# второй вариант усложнен в том, что массив обходится в 2 раза, то есть O(n ** 2)
# третий вариант на мой взгляд саммый оптимальный из трех и этому доказательство время выполнения


def p1():
    number = [str(i) for i in range(10000)]
    first_list = []
    second_list = []

    for num in number:
        if int(num) % 2 == 0:
            first_list.append(num)

    for num in number:
        if int(num) % 2 != 0:
            second_list.append(num)


cProfile.run("p1()")

#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#       1    0.007    0.007    0.011    0.011 Task1.py:66(p1)
#       1    0.003    0.003    0.003    0.003 Task1.py:67(<listcomp>)
#       1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#   10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def p2():
    number = [i for i in range(10000)]
    first_list = []
    second_list = []

    for num in number:
        if num % 2 == 0:
            first_list.append(num)

    for num in number:
        if num % 2 != 0:
            second_list.append(num)


cProfile.run("p2()")

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.002    0.002    0.003    0.003 Task1.py:94(p2)
#         1    0.001    0.001    0.001    0.001 Task1.py:95(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def p3():
    number = [i for i in range(10000)]
    first_list = []
    second_list = []
    for num in number:
        if num % 2 == 0:
            first_list.append(num)
        else:
            second_list.append(num)


cProfile.run("p3()")


#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 Task1.py:120(p3)
#         1    0.000    0.000    0.000    0.000 Task1.py:121(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#     10000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

