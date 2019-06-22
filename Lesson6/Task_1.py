# Определить, какое число в массиве встречается чаще всего.

import random
import sys


rand_list = [random.randint(0, 100) for i in range(10)]
print(rand_list)

count = 1
number = 0
memory = 0

for i in rand_list:
    memory += sys.getsizeof(i)
    temp_count = 0

    for j in rand_list:

        if i == j:
            temp_count += 1

    if count < temp_count:
        number = i
        count = temp_count


if count > 1:
    print(f"Чаще всего встречается число {number}, количество совпадений: {count}")

else:
    print("Совпадений в массиве нет")


memory +=  sys.getsizeof(count) + sys.getsizeof(rand_list)

print(f"размер употребляемой памяти: {memory} байт")


# Чаще всего встречается число 11, количество совпадений: 2
# размер употребляемой памяти: 528 байт

# Совпадений в массиве нет
# размер употребляемой памяти: 524 байт

# Здесь в отличии от второго варианта значение употребляемой памяти не меняется
# в результате совпаддений, значение колеблится из за переменной number и нулей в случайном списке,
# так как 0 требует 24 байта а единица уже 28 байт.
