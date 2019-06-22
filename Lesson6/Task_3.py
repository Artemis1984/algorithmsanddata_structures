
from collections import deque
import random
import sys


rand_list = deque([random.randint(0, 100) for i in range(10)])
print(rand_list)
number = {}
memory = 0

for i in rand_list:
    memory_temp = rand_list.count(i)
    if memory_temp > 1:
        number.__setitem__(i, memory_temp)


for i in rand_list:
    memory += sys.getsizeof(i)

memory += sys.getsizeof(rand_list) + sys.getsizeof(number) + sys.getsizeof(memory)

if len(number) != 0:
    print(f"Совподений: {len(number)}, {number}")
    print(f"размер употребляемой памяти: {memory} байт")

else:
    print(f"Нет совпадений")
    print(f"размер употребляемой памяти: {memory} байт")

# Совподений: 1, {26: 2}
# размер употребляемой памяти: 1180 байт

# Совподений: 2, {33: 2, 80: 2}
# размер употребляемой памяти: 1180 байт

# Нет совпадений
# размер употребляемой памяти: 1176 байт, отличие в том,
# что в массиве сгенерировано случайное число 0




