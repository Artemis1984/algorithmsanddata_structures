# Попробуем использовать другой алгоритм и измерирм память

from collections import Counter
import random
import sys

rand_list = Counter([random.randint(0, 100) for i in range(10)])

print(rand_list)

if max(rand_list.values()) > 1:
    for k in rand_list:
        if rand_list.get(k) > 1:
            print("число", k, "повторяется", rand_list.get(k), "раза")

else:
    print("Нет совпадений")

memory = 0

for i in rand_list.items():

    memory += sys.getsizeof(i)

memory += sys.getsizeof(rand_list)

print(f"размер употребляемой памяти: {memory} байт")


# Нет совпадений
# размер употребляемой памяти: 1024 байт

# число 37 повторяется 2 раза
# размер употребляемой памяти: 960 байт

# число 33 повторяется 2 раза
# число 85 повторяется 2 раза
# размер употребляемой памяти: 896 байт

# Словарь употребляет больше памяти чем список и в случае совпаний в словарь помещается меньше
# элементов в результате чего употребляется меньше памяти.

