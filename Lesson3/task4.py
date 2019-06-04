# Определить, какое число в массиве встречается чаще всего.
import random

rand_list = [random.randint(0, 100) for i in range(10)]
print(rand_list)

count = 1
number = 0

for i in rand_list:

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
